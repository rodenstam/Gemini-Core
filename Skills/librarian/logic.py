import os
import shutil
import yaml
import re
from datetime import datetime
from pathlib import Path
from rules import RULES, is_ignored
from semantic_helper import SemanticHelper

class LibrarianLogic:
    def __init__(self, root_dir):
        self.root = Path(root_dir)
        self.issues = []
        self.manifest_data = {}
        self.semantic = SemanticHelper(root_dir)

    def _load_yaml(self, file_path):
        try:
            # Use utf-8-sig to handle potential BOM
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
                # Remove leading whitespace including BOM if any
                content = content.lstrip()
                match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                if match:
                    return yaml.safe_load(match.group(1))
        except:
            pass
        return None

    def _set_yaml(self, file_path, data):
        """Injects or updates YAML frontmatter in a file."""
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
            
            # Check for existing YAML
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            yaml_block = f"---\n{yaml.dump(data, allow_unicode=True)}---\n"
            
            if match:
                # Replace existing
                new_content = yaml_block + content[match.end():].lstrip()
            else:
                # Prepend new
                new_content = yaml_block + content.lstrip()
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f"❌ Fel vid skrivning av YAML till {file_path}: {e}")
            return False

    def audit_structure(self):
        """Checks for misplaced files in the root."""
        print("🔍 Granskar rotkatalogen...")
        allowed_dirs = RULES["STRUCTURE"]["ALLOWED_ROOT_DIRS"]
        allowed_files = RULES["STRUCTURE"]["ALLOWED_ROOT_FILES"]
        misplaced = []
        
        for item in self.root.iterdir():
            if is_ignored(item, self.root):
                continue
            
            is_misplaced = False
            if item.is_dir():
                if item.name not in allowed_dirs:
                    is_misplaced = True
                    self.issues.append(f"[STRUKTUR] Okänd mapp i roten: {item.name}")
            else:
                if item.name not in allowed_files:
                    is_misplaced = True
                    self.issues.append(f"[STRUKTUR] Lös fil i roten: {item.name}")
            
            if is_misplaced:
                misplaced.append(item)
        return misplaced

    def audit_documentation(self):
        """Validates project and skill documentation tiers."""
        print("🔍 Granskar dokumentations-tiers...")
        
        # Projects
        proj_dir = self.root / "Projects"
        if proj_dir.exists():
            for p in proj_dir.iterdir():
                if p.is_dir() and not is_ignored(p, self.root):
                    self._check_project(p)

        # Skills
        skill_dir = self.root / "Skills"
        if skill_dir.exists():
            for s in skill_dir.iterdir():
                if s.is_dir() and not is_ignored(s, self.root):
                    self._check_skill(s)

    def _check_project(self, path):
        manifest_path = path / RULES["DOCUMENTATION"]["MANIFEST_FILENAME"]
        if not manifest_path.exists():
            self.issues.append(f"[DOCS] Projekt saknar manifest: {path.name}")
            return

        data = self._load_yaml(manifest_path)
        if not data:
            self.issues.append(f"[DOCS] Kunde inte läsa manifest för {path.name}")
            return

        tier = data.get('type')
        if tier == RULES["DOCUMENTATION"]["LITE_TIER_TYPE"]:
            return # Lite Tier is okay with just GEMINI.md
        
        # Full Tier check
        docs_dir = path / "docs"
        if not docs_dir.exists():
            self.issues.append(f"[DOCS] Full-tier projekt saknar docs-mapp: {path.name}")
        else:
            for req_file in RULES["DOCUMENTATION"]["FULL_TIER_FILES"]:
                if not (docs_dir / req_file).exists():
                    self.issues.append(f"[DOCS] Saknar {req_file} i {path.name}/docs/")

    def _check_skill(self, path):
        manifest_path = path / RULES["DOCUMENTATION"]["SKILL_MANIFEST_FILENAME"]
        if not manifest_path.exists():
            self.issues.append(f"[DOCS] Skill saknar SKILL.md: {path.name}")

    def audit_plans(self):
        """Checks strategy and active plans for YAML status and dates."""
        print("🔍 Granskar planer i Strategy och Plans...")
        
        # 1. Drafts
        draft_dir = self.root / RULES["PLANNING"]["DRAFT_DIR"]
        if draft_dir.exists():
            for plan in draft_dir.glob("*.md"):
                self._check_plan_yaml(plan)

        # 2. Active
        for status, rel_path in RULES["PLANNING"]["ACTIVE_DIRS"].items():
            active_dir = self.root / rel_path
            if active_dir.exists():
                for plan in active_dir.glob("*.md"):
                    self._check_plan_yaml(plan)

    def _check_plan_yaml(self, plan_path):
        """Helper to validate plan YAML."""
        data = self._load_yaml(plan_path)
        if not data:
            self.issues.append(f"[PLAN] Plan saknar YAML-status: {plan_path.name}")
            return
        
        for field in RULES["PLANNING"]["REQUIRED_YAML_FIELDS"]:
            if field not in data:
                self.issues.append(f"[PLAN] Plan saknar fält '{field}': {plan_path.name}")
        
        status = data.get('status')
        if status not in RULES["PLANNING"]["VALID_STATUSES"]:
            self.issues.append(f"[PLAN] Ogiltig status '{status}' i {plan_path.name}")

    def audit_archive(self):
        """Ensures all archived plans follow the YYYY-MM-DD_Filename.md pattern."""
        print("🔍 Granskar arkivet (Archive/Plans)...")
        archive_root = self.root / "Workspace/Archive/Plans"
        if not archive_root.exists():
            return

        date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}_')
        valid_subdirs = set(RULES["PLANNING"]["ARCHIVE_DIRS"].values())

        for item in archive_root.iterdir():
            if is_ignored(item, self.root):
                continue
            
            if item.is_dir():
                rel_item = os.path.relpath(item, self.root).replace("\\", "/")
                if rel_item not in valid_subdirs:
                    self.issues.append(f"[ARKIV] Okänd undermapp i arkivet: {item.name}")
                    continue
                
                for plan in item.glob("*.md"):
                    if not date_pattern.match(plan.name):
                        self.issues.append(f"[ARKIV] Fil saknar datum-prefix: {item.name}/{plan.name}")
            else:
                self.issues.append(f"[ARKIV] Lös fil i arkivets rot: {item.name}")

    def run_audit(self):
        self.audit_structure()
        self.audit_documentation()
        self.audit_plans()
        self.audit_archive()
        
        if not self.issues:
            print("\n✨ Allt ser perfekt ut! Bibliotekarien är nöjd.")
        else:
            print(f"\n⚠️ Hittade {len(self.issues)} problem:")
            for issue in self.issues:
                print(f"  {issue}")

    def archive_plan(self, plan_filename):
        """Archives a plan by moving it to the correct archive folder based on status."""
        # 1. Find the plan
        plan_path = None
        
        # Check Drafts
        draft_path = self.root / RULES["PLANNING"]["DRAFT_DIR"] / plan_filename
        if draft_path.exists():
            plan_path = draft_path
        else:
            # Check Active
            for rel_path in RULES["PLANNING"]["ACTIVE_DIRS"].values():
                p = self.root / rel_path / plan_filename
                if p.exists():
                    plan_path = p
                    break
        
        if not plan_path:
            print(f"❌ Fel: Hittade inte {plan_filename} i Strategy eller Plans.")
            return

        # 2. Determine target
        data = self._load_yaml(plan_path)
        status = data.get("status") if data else "slutförd"
        
        archive_rel_path = RULES["PLANNING"]["ARCHIVE_DIRS"].get(status, "Workspace/Archive/Plans/Slutförda")
        target_dir = self.root / archive_rel_path
        target_dir.mkdir(parents=True, exist_ok=True)

        # 3. Calculate new name
        today = datetime.now().strftime("%Y-%m-%d")
        # Ensure we don't double-prefix if it already has one
        if not re.match(r'^\d{4}-\d{2}-\d{2}_', plan_filename):
            new_name = f"{today}_{plan_filename}"
        else:
            new_name = plan_filename
            
        dest_path = target_dir / new_name

        # 4. Move
        shutil.move(str(plan_path), str(dest_path))
        print(f"📦 Arkiverad: {plan_filename} -> {archive_rel_path}/{new_name}")
        
        # Trigger mirror
        os.system(f"python Skills/mirror/mirror.py")

    def run_tidy(self):
        print("🧹 Påbörjar systemstädning (Tidy Mode)...")
        misplaced = self.audit_structure()
        self.audit_documentation()
        self.audit_plans()
        self.audit_archive()
        
        if misplaced:
            print(f"\n🧩 Analyserar {len(misplaced)} lösa objekt för sorteringsförslag...")
            for item in misplaced:
                rel_path = os.path.relpath(item, self.root)
                suggestions = self.semantic.get_best_home(rel_path)
                
                print(f"\n📂 Objekt: {rel_path}")
                if suggestions:
                    print("   Förslag på plats:")
                    for s in suggestions:
                        print(f"   - [{s['score']:.4f}] {s['home']}")
                else:
                    print("   (Kunde inte hitta ett bra semantiskt hem. Är filen indexerad?)")
        
        print("\n--- Tidy genomgång klar ---")

    def _extract_title(self, file_path):
        """Extracts the first H1 header from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("# "):
                        # Remove emojis and the # prefix
                        title = re.sub(r'[^\w\s\-\(\)\.]', '', line[2:]).strip()
                        return title
        except:
            pass
        return os.path.splitext(os.path.basename(file_path))[0]

    def _calculate_status_from_tasks(self, file_path):
        """Derives status based on markdown checkboxes [ ] vs [x]."""
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
            
            total_tasks = len(re.findall(r'-\s*\[[ xX]\]', content))
            completed_tasks = len(re.findall(r'-\s*\[[xX]\]', content))
            
            if total_tasks == 0:
                return None # No tasks found, keep existing status
            
            if completed_tasks == total_tasks:
                return "slutförd"
            elif completed_tasks > 0:
                return "pågående"
            else:
                return "planerad"
        except:
            return None

    def run_fix(self):
        print("🔧 Påbörjar automatisk korrigering (Fix Mode)...")
        fixed_count = 0
        today_str = datetime.now().strftime("%Y-%m-%d")

        # Helper to check if data has all required fields
        def needs_update(data):
            if not data: return True
            return any(field not in data for field in RULES["PLANNING"]["REQUIRED_YAML_FIELDS"])

        # 1. Handle Archive Naming and YAML
        archive_root = self.root / "Workspace/Archive/Plans"
        if archive_root.exists():
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}_')
            # Check all subdirs in Archive
            for status_dir in RULES["PLANNING"]["ARCHIVE_DIRS"].values():
                full_status_dir = self.root / status_dir
                if not full_status_dir.exists(): continue
                
                for plan in full_status_dir.glob("*.md"):
                    current_path = plan
                    # A. Fix Name
                    if not date_pattern.match(plan.name):
                        mtime = datetime.fromtimestamp(os.path.getmtime(plan))
                        date_str = mtime.strftime("%Y-%m-%d")
                        new_name = f"{date_str}_{plan.name}"
                        current_path = plan.parent / new_name
                        print(f"✅ Fixar namn: {plan.name} -> {new_name}")
                        os.rename(plan, current_path)
                        fixed_count += 1
                    
                    # B. Fix YAML content (Rich Metadata)
                    data = self._load_yaml(current_path) or {}
                    calculated_status = self._calculate_status_from_tasks(current_path)
                    
                    if needs_update(data) or (calculated_status and data.get("status") != calculated_status):
                        mtime = datetime.fromtimestamp(os.path.getmtime(current_path))
                        date_str = mtime.strftime("%Y-%m-%d")
                        
                        rich_data = {
                            "id": data.get("id") or current_path.stem.lower().replace('_', '-'),
                            "title": data.get("title") or self._extract_title(current_path),
                            "status": calculated_status or data.get("status") or "slutförd",
                            "created": data.get("created") or date_str,
                            "updated": data.get("updated") or date_str,
                            "version": data.get("version") or 1.0,
                            "priority": data.get("priority") or "medel",
                            "tags": data.get("tags") or []
                        }
                        if self._set_yaml(current_path, rich_data):
                            print(f"📝 Uppdaterade rik metadata & status i arkiv-fil: {current_path.name}")
                            fixed_count += 1

        # 2. Handle Strategy and Plans (Moving files to correct homes)
        search_dirs = [self.root / RULES["PLANNING"]["DRAFT_DIR"]]
        for active_rel in RULES["PLANNING"]["ACTIVE_DIRS"].values():
            search_dirs.append(self.root / active_rel)
            
        for s_dir in search_dirs:
            if not s_dir.exists(): continue
            for plan in s_dir.glob("*.md"):
                data = self._load_yaml(plan) or {}
                calculated_status = self._calculate_status_from_tasks(plan)
                status = calculated_status or data.get("status") or "utkast"
                
                # Update YAML if needed
                if needs_update(data) or status != data.get("status"):
                    rich_data = {
                        "id": data.get("id") or plan.stem.lower().replace('_', '-'),
                        "title": data.get("title") or self._extract_title(plan),
                        "status": status,
                        "created": data.get("created") or today_str,
                        "updated": today_str,
                        "version": data.get("version") or 1.0,
                        "priority": data.get("priority") or "medel",
                        "tags": data.get("tags") or []
                    }
                    self._set_yaml(plan, rich_data)
                    fixed_count += 1

                # Move to correct home if misplaced
                target_rel = None
                if status in RULES["PLANNING"]["ACTIVE_DIRS"]:
                    target_rel = RULES["PLANNING"]["ACTIVE_DIRS"][status]
                elif status == "utkast":
                    target_rel = RULES["PLANNING"]["DRAFT_DIR"]
                elif status in RULES["PLANNING"]["ARCHIVE_DIRS"]:
                    # If it's slutförd or avbruten, move to archive!
                    target_rel = RULES["PLANNING"]["ARCHIVE_DIRS"][status]
                
                if target_rel:
                    target_dir = self.root / target_rel
                    if not target_dir.exists(): target_dir.mkdir(parents=True, exist_ok=True)
                    
                    if s_dir != target_dir:
                        # Add date prefix if moving to archive
                        new_name = plan.name
                        if status in RULES["PLANNING"]["ARCHIVE_DIRS"] and not date_pattern.match(new_name):
                            new_name = f"{today_str}_{new_name}"
                            
                        print(f"🚚 Flyttar {plan.name} -> {target_rel}/")
                        shutil.move(str(plan), str(target_dir / new_name))
                        fixed_count += 1
        
        print(f"\n--- Fix klar! {fixed_count} åtgärder genomförda. ---")
        os.system(f"python Skills/mirror/mirror.py")
