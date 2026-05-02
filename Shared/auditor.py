import os
import yaml
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta

class Auditor:
    """
    Gemini-Core v4.0 System Auditor.
    Validates manifests, checks dependencies, generates dependency graphs, 
    and detects zombie projects.
    """
    def __init__(self, root_dir):
        self.root = os.path.normpath(root_dir)
        self.manifests = {}  # absolute_path -> data
        self.report = []
        self.dependency_graph = {}
        self.zombies = []

    def find_manifests(self):
        """Discovers all GEMINI.md and SKILL.md files and parses their YAML."""
        targets = [
            (self.root, "GEMINI.md"),
            (os.path.join(self.root, "Projects"), "GEMINI.md"),
            (os.path.join(self.root, "Skills"), "SKILL.md")
        ]

        for base_dir, filename in targets:
            if not os.path.exists(base_dir):
                continue
            
            if base_dir == self.root:
                # Root level
                self._process_file(os.path.join(base_dir, filename))
            else:
                # Subdirectories (Projects or Skills)
                for item in os.listdir(base_dir):
                    item_path = os.path.join(base_dir, item)
                    if os.path.isdir(item_path):
                        self._process_file(os.path.join(item_path, filename))

    def _process_file(self, file_path):
        if os.path.exists(file_path):
            data = self.parse_manifest(file_path)
            if data:
                self.manifests[file_path] = data

    def parse_manifest(self, file_path):
        """Extracts and parses YAML frontmatter from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                if match:
                    yaml_str = match.group(1)
                    return yaml.safe_load(yaml_str)
                else:
                    self.report.append(f"[!] {os.path.relpath(file_path, self.root)}: No YAML frontmatter found.")
                    return None
        except Exception as e:
            self.report.append(f"[ERROR] {os.path.relpath(file_path, self.root)}: Failed to parse YAML: {e}")
            return None

    def validate_manifests(self):
        """Checks for required fields and valid dependency paths."""
        for path, data in self.manifests.items():
            rel_path = os.path.relpath(path, self.root)
            manifest_type = data.get('type', 'unknown')

            # 1. Check Required Fields based on type
            if manifest_type == 'lite':
                required_fields = ['version', 'type', 'status', 'updated']
            else:
                required_fields = ['version', 'type', 'dependencies', 'stats']
            
            for field in required_fields:
                if field not in data:
                    self.report.append(f"[-] {rel_path}: Missing required field '{field}'.")

            # 2. Validate "Engineering Four" for standard projects
            if manifest_type == 'project':
                project_dir = os.path.dirname(path)
                docs_dir = os.path.join(project_dir, "docs")
                core_four = ["SPECS.md", "TASKS.md", "LOG.md", "DECISIONS.md"]
                if not os.path.exists(docs_dir):
                    self.report.append(f"[-] {rel_path}: Missing 'docs/' directory.")
                else:
                    for doc in core_four:
                        if not os.path.exists(os.path.join(docs_dir, doc)):
                            self.report.append(f"[-] {rel_path}: Missing '{doc}' in docs/.")

            # 3. Validate Dependencies
            deps = data.get('dependencies', [])
            if not isinstance(deps, list):
                if manifest_type != 'lite': # Lite manifests might not have dependencies
                    self.report.append(f"[-] {rel_path}: 'dependencies' should be a list.")
                continue

            node_name = self._get_node_name(path, data)
            self.dependency_graph[node_name] = []

            for dep in deps:
                if not isinstance(dep, dict) or len(dep) != 1:
                    self.report.append(f"[-] {rel_path}: Invalid dependency format: {dep}")
                    continue
                
                dep_type, dep_val = list(dep.items())[0]
                valid = self._check_dependency(dep_type, dep_val)
                if not valid:
                    self.report.append(f"[❌] {rel_path}: Broken dependency -> {dep_type}: {dep_val}")
                else:
                    self.dependency_graph[node_name].append(f"{dep_type}:{dep_val}")

    def _get_node_name(self, path, data):
        """Returns a unique name for the manifest node."""
        rel_path = os.path.relpath(path, self.root)
        if data.get('type') == 'core':
            return "core"
        parts = rel_path.split(os.sep)
        if len(parts) >= 2:
            return f"{data.get('type')}:{parts[1]}"
        return rel_path

    def _check_dependency(self, dep_type, dep_val):
        """Checks if a dependency target exists."""
        if dep_type == 'skill':
            path = os.path.join(self.root, "Skills", dep_val, "SKILL.md")
            return os.path.exists(path)
        elif dep_type == 'shared':
            path = os.path.join(self.root, "Shared", dep_val)
            return os.path.exists(path)
        elif dep_type == 'project':
            path = os.path.join(self.root, "Projects", dep_val, "GEMINI.md")
            return os.path.exists(path)
        return False

    def detect_zombies(self, days=60):
        """Identifies projects with no LOG.md updates in the last X days."""
        projects_dir = os.path.join(self.root, "Projects")
        if not os.path.exists(projects_dir):
            return

        for project in os.listdir(projects_dir):
            p_path = os.path.join(projects_dir, project)
            if not os.path.isdir(p_path):
                continue
            
            log_path = os.path.join(p_path, "docs", "LOG.md")
            if os.path.exists(log_path):
                mtime = datetime.fromtimestamp(os.path.getmtime(log_path))
                if datetime.now() - mtime > timedelta(days=days):
                    self.zombies.append(f"{project} (Last active: {mtime.strftime('%Y-%m-%d')})")
            else:
                # If no LOG.md, check directory mtime as fallback
                mtime = datetime.fromtimestamp(os.path.getmtime(p_path))
                if datetime.now() - mtime > timedelta(days=days):
                    self.zombies.append(f"{project} (No LOG.md, directory stale since: {mtime.strftime('%Y-%m-%d')})")

    def save_results(self):
        """Writes the dependency graph to Data/dependency_graph.json."""
        data_dir = os.path.join(self.root, "Data")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        graph_path = os.path.join(data_dir, "dependency_graph.json")
        try:
            with open(graph_path, 'w', encoding='utf-8') as f:
                json.dump(self.dependency_graph, f, indent=4)
            return True
        except Exception as e:
            self.report.append(f"[ERROR] Failed to save dependency graph: {e}")
            return False

    def _trigger_mirror(self):
        """Runs the mirror skill in the background."""
        print("🪞 Triggering Background Mirroring...")
        mirror_script = os.path.join(self.root, "Skills", "mirror", "mirror.py")
        try:
            # Run mirror.py in the background
            subprocess.Popen([sys.executable, mirror_script], 
                             stdout=subprocess.DEVNULL, 
                             stderr=subprocess.DEVNULL,
                             creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
            print("✅ Mirroring process started in background.")
        except Exception as e:
            print(f"[-] Failed to trigger mirror: {e}")

    def run(self, trigger_mirror=False):
        """Executes the full audit process."""
        print(f"--- Gemini Core Auditor v4.0 | {datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
        
        self.find_manifests()
        self.validate_manifests()
        self.detect_zombies()
        self.save_results()

        # Output Report
        if not self.report and not self.zombies:
            print("✅ SYSTEM HEALTHY: All manifests and dependencies are valid.")
            if trigger_mirror:
                self._trigger_mirror()
        else:
            if self.report:
                print(f"\nIssues Found ({len(self.report)}):")
                for issue in self.report:
                    print(f"  {issue}")
            
            if self.zombies:
                print(f"\nZombie Projects Detected ({len(self.zombies)}):")
                for zombie in self.zombies:
                    print(f"  [🧟] {zombie}")

        print(f"\nDependency Graph updated: Data/dependency_graph.json")
        print("--- Audit Complete ---")

if __name__ == "__main__":
    # Assumes script is in Shared/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.normpath(os.path.join(script_dir, ".."))
    
    # Check if --mirror flag is passed
    trigger_mirror = "--mirror" in sys.argv
    
    auditor = Auditor(root_dir)
    auditor.run(trigger_mirror=trigger_mirror)
