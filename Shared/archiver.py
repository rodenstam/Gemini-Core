import os
import shutil
import json
import re
from pathlib import Path
from datetime import datetime

class Archiver:
    """
    Gemini-Core v4.0 Archiver Tool.
    Automates the Selective Archiving protocol for plans and milestone folders.
    """
    def __init__(self, root_dir):
        self.root = Path(root_dir).absolute()
        self.workspace_root = self.root / "Workspace"
        self.archive_root = self.workspace_root / "Archive" / "Plans"
        self.strategy_root = self.workspace_root / "Strategy"

    def archive_plan(self, plan_filename, milestone_name):
        """
        Packages a plan and its context (LOG, DECISIONS) into a milestone folder.
        """
        plan_path = self.strategy_root / plan_filename
        if not plan_path.exists():
            # Fallback to Workspace root if not in Strategy
            plan_path = self.workspace_root / plan_filename
            if not plan_path.exists():
                print(f"❌ Error: Plan {plan_filename} not found.")
                return False

        # 1. Create Milestone Directory
        target_dir = self.archive_root / milestone_name
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 Created milestone folder: {target_dir.relative_to(self.root)}")

        # 2. Move core files
        # We look for DECISIONS.md and LOG.md in Strategy as well
        files_to_move = [plan_path]
        
        # Possible associated files in Strategy or Workspace root
        context_files = ["DECISIONS.md", "LOG.md", "LOGS.md"]
        for cf in context_files:
            cp = self.strategy_root / cf
            if cp.exists():
                files_to_move.append(cp)
            else:
                cp = self.workspace_root / cf
                if cp.exists():
                    files_to_move.append(cp)

        for f in files_to_move:
            dest = target_dir / f.name
            shutil.move(str(f), str(dest))
            print(f"📦 Archived: {f.name} -> {milestone_name}/")

        return True

    def cleanup_strategy(self, exclude_files=None):
        """
        Identifies remaining files in Strategy and prompts for deletion.
        """
        if not self.strategy_root.exists():
            return

        exclude = exclude_files or []
        remaining = [f for f in self.strategy_root.glob("*.md") if f.name not in exclude]

        if not remaining:
            print("✨ Strategy folder is already clean.")
            return

        print("\n🧹 Remaining files in Strategy:")
        for f in remaining:
            print(f"  - {f.name}")
        
        print("\n[!] Manual cleanup recommended for non-essential materials.")

    def run_mirror(self):
        """Triggers the mirror skill."""
        print("\n🪞 Syncing to Obsidian...")
        mirror_script = self.root / "Skills" / "mirror" / "mirror.py"
        if mirror_script.exists():
            os.system(f"python \"{mirror_script}\"")
        else:
            print("[-] Mirror script not found.")

if __name__ == "__main__":
    import sys
    # Assumes script is in Shared/
    script_dir = Path(__file__).parent.absolute()
    root_dir = script_dir.parent
    
    archiver = Archiver(root_dir)
    
    if len(sys.argv) < 3:
        print("Usage: python archiver.py --archive <plan_file> <milestone_name>")
        sys.exit(1)
        
    if sys.argv[1] == "--archive":
        plan_file = sys.argv[2]
        milestone = sys.argv[3]
        if archiver.archive_plan(plan_file, milestone):
            archiver.cleanup_strategy(exclude_files=[plan_file])
            archiver.run_mirror()

