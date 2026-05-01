import os
import shutil
import json
from pathlib import Path

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
            "Workspace": "Management",
            "Projects": "Projects",
            "Skills": "Knowledge",
            "docs": "System/docs"
        }
        
        self.allowed_extensions = {'.md', '.pdf', '.png', '.jpg', '.jpeg', '.gif'}

    def get_mirror_path(self, local_path):
        """Calculates the target path in Obsidian based on mapping rules."""
        local_path = Path(local_path).absolute()
        
        # Find relative path from source root
        try:
            rel_path = local_path.relative_to(self.source_root)
        except ValueError:
            return None # File is outside source root
            
        parts = list(rel_path.parts)
        
        if not parts:
            return self.mirror_root
            
        # Check if first part of path is in our mappings
        if parts[0] in self.mappings:
            parts[0] = self.mappings[parts[0]]
            
        return self.mirror_root.joinpath(*parts)

    def mirror_file(self, file_path):
        """Mirrors a single file if it matches the criteria."""
        file_path = Path(file_path)
        
        if file_path.suffix.lower() not in self.allowed_extensions:
            return False
            
        target_path = self.get_mirror_path(file_path)
        if not target_path:
            return False
            
        # Ensure target directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        try:
            shutil.copy2(file_path, target_path)
            print(f" mirrored: {file_path.name} -> {target_path.relative_to(self.mirror_root)}")
            return True
        except Exception as e:
            print(f" error mirroring {file_path.name}: {e}")
            return False

    def mirror_all(self):
        """Performs a full mirror of all allowed files in mapped directories."""
        print(f"🚀 Starting full mirror to {self.mirror_root}...")
        count = 0
        
        # Mirror root level .md files
        for file in self.source_root.glob("*.md"):
            if self.mirror_file(file):
                count += 1
                
        # Mirror mapped directories
        for local_dir in self.mappings.keys():
            dir_path = self.source_root / local_dir
            if dir_path.exists():
                for file in dir_path.rglob("*"):
                    if file.is_file() and "__pycache__" not in str(file):
                        if self.mirror_file(file):
                            count += 1
                            
        print(f"✅ Mirror complete. {count} files processed.")

if __name__ == "__main__":
    # Quick test execution
    mirror = MirrorSkill()
    mirror.mirror_all()
