import os
import re
import json
from datetime import datetime, timedelta

class CoreAuditor:
    """
    Architectural Guardian for Gemini Core.
    Ensures that the project follows the v2.1+ standards regarding 
    structure, documentation, and link integrity.
    """
    def __init__(self, root_path):
        self.root = os.path.normpath(root_path)
        self.report = []
        self.projects = []
        self.system_dirs = ['Engine', 'Data', 'Rules', 'docs', 'Skills', 'arbetsyta']

    def scan_projects(self):
        """Identifies project folders in the root directory."""
        try:
            entries = os.listdir(self.root)
            self.projects = [d for d in entries 
                            if os.path.isdir(os.path.join(self.root, d)) 
                            and not d.startswith('.') 
                            and d not in self.system_dirs]
        except Exception as e:
            self.report.append(f"[FATAL] Could not read root directory: {e}")

    def validate_core_four(self, project):
        """Checks if 'The Core Four' documentation exists in the project/docs/ folder."""
        docs_path = os.path.join(self.root, project, 'docs')
        core_four = ['tasks.md', 'pins.md', 'devlog.md', 'roadmap.md']
        
        if not os.path.exists(docs_path):
            self.report.append(f"[!] {project}: Missing 'docs/' folder.")
            return

        for doc in core_four:
            if not os.path.exists(os.path.join(docs_path, doc)):
                self.report.append(f"[-] {project}: Missing documentation: {doc}")

    def verify_engine_links(self, project):
        """Verifies that python commands in GEMINI.md point to existing scripts in Engine/."""
        gemini_path = os.path.join(self.root, project, 'GEMINI.md')
        if not os.path.exists(gemini_path):
            self.report.append(f"[!] {project}: Missing GEMINI.md (Project Front Door).")
            return

        with open(gemini_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Regex to find relative paths pointing to Engine (e.g., ../../Engine/...)
            links = re.findall(r'(\.\.\/\.\.\/Engine\/[\w\/\.-]+\.py)', content)
            
            for link in links:
                # Convert relative path to absolute for validation
                abs_path = os.path.normpath(os.path.join(self.root, project, link))
                if not os.path.exists(abs_path):
                    self.report.append(f"[❌] {project}: Broken link in GEMINI.md -> {link}")

    def check_staleness(self, project, days=30):
        """Flags projects that haven't been touched in a while (based on devlog.md)."""
        devlog_path = os.path.join(self.root, project, 'docs', 'devlog.md')
        if os.path.exists(devlog_path):
            mtime = datetime.fromtimestamp(os.path.getmtime(devlog_path))
            if datetime.now() - mtime > timedelta(days=days):
                self.report.append(f"[?] {project}: Stale (last active: {mtime.strftime('%Y-%m-%d')}). Consider archiving.")

    def run_audit(self):
        """Executes the full audit suite."""
        print(f"--- Gemini Core Auditor v0.1 | {datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
        print(f"Scanning: {self.root}\n")
        
        self.scan_projects()
        if not self.projects:
            print("No projects found to audit.")
            return

        for p in self.projects:
            self.validate_core_four(p)
            self.verify_engine_links(p)
            self.check_staleness(p)
        
        if not self.report:
            print("✅ SYSTEM HEALTHY: All projects adhere to v2.1 standards.")
        else:
            print(f"Found {len(self.report)} issues/suggestions:")
            for issue in self.report:
                print(issue)
        print("\n--- Audit Complete ---")

if __name__ == "__main__":
    # Path is relative to the script's location in Engine/Shared/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.normpath(os.path.join(script_dir, "../../"))
    
    auditor = CoreAuditor(root_dir)
    auditor.run_audit()
