import os
import shutil
import json
from pathlib import Path
from datetime import datetime

class MirrorSkill:
    def __init__(self, settings_path="settings.json"):
        # Use absolute path for settings if possible
        base_dir = Path(__file__).parent.parent.parent
        settings_file = base_dir / settings_path
        
        with open(settings_file, 'r') as f:
            self.settings = json.load(f)
        
        self.source_root = Path(self.settings['paths']['source_root'])
        self.mirror_root = Path(self.settings['paths']['mirror_root'])
        
        # Mapping rules: local_subdir -> obsidian_subdir
        self.mappings = {
            "Workspace": "Workspace",
            "Projects": "Projects",
            "Skills": "Skills",
            "docs": "System/docs"
        }
        
        self.allowed_extensions = {'.md', '.pdf', '.png', '.jpg', '.jpeg', '.gif'}

    def get_mirror_path(self, local_path, root_override=None):
        """Calculates the target path in Obsidian based on mapping rules."""
        base_root = root_override if root_override else self.mirror_root
        local_path = Path(local_path).absolute()
        
        try:
            rel_path = local_path.relative_to(self.source_root)
        except ValueError:
            return None
            
        parts = list(rel_path.parts)
        if not parts:
            return base_root
            
        if parts[0] in self.mappings:
            parts[0] = self.mappings[parts[0]]
            
        return base_root.joinpath(*parts)

    def generate_status_badge(self, success, count):
        """Creates MIRROR_STATUS.md in the mirror root."""
        status_path = self.mirror_root / "MIRROR_STATUS.md"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "✅ Healthy" if success else "❌ Failed"
        
        content = f"""# 🪞 Mirror Status
- **Status:** {status}
- **Last Sync:** {timestamp}
- **Files Processed:** {count}
- **Engine:** Gemini-Core v4.0 (Atomic Stage-and-Swap)
"""
        try:
            status_path.parent.mkdir(parents=True, exist_ok=True)
            with open(status_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error generating status badge: {e}")

    def mirror_all(self):
        """Performs a Stage-and-Swap mirror for atomic updates."""
        print(f"🚀 Starting atomic mirror to {self.mirror_root}...")
        
        staging_dir = self.mirror_root.parent / ".mirror_staging"
        if staging_dir.exists():
            shutil.rmtree(staging_dir)
        staging_dir.mkdir(parents=True, exist_ok=True)
        
        count = 0
        success = True
        
        try:
            # 1. Populate Staging
            # Root files
            for file in self.source_root.glob("*.md"):
                if file.is_file() and file.suffix.lower() in self.allowed_extensions:
                    target = self.get_mirror_path(file, root_override=staging_dir)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file, target)
                    count += 1
            
            # Mapped directories
            for local_dir in self.mappings.keys():
                dir_path = self.source_root / local_dir
                if dir_path.exists():
                    for file in dir_path.rglob("*"):
                        if file.is_file() and "__pycache__" not in str(file):
                            if file.suffix.lower() in self.allowed_extensions:
                                target = self.get_mirror_path(file, root_override=staging_dir)
                                target.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(file, target)
                                count += 1

            # 2. Swap (Atomic-ish)
            # We swap top-level directories and root files
            for item in os.listdir(staging_dir):
                s_item = staging_dir / item
                d_item = self.mirror_root / item
                
                if d_item.exists():
                    if d_item.is_dir():
                        shutil.rmtree(d_item)
                    else:
                        os.remove(d_item)
                
                if s_item.is_dir():
                    shutil.move(str(s_item), str(d_item))
                else:
                    shutil.move(str(s_item), str(d_item))

            print(f"✅ Atomic mirror complete. {count} files processed.")
        except Exception as e:
            print(f"❌ Mirror failed: {e}")
            success = False
        finally:
            if staging_dir.exists():
                shutil.rmtree(staging_dir)
            self.generate_status_badge(success, count)

if __name__ == "__main__":
    mirror = MirrorSkill()
    mirror.mirror_all()
