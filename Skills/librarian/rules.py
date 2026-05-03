import os

# Gemini-Core PARA/Engineering Standards
RULES = {
    "STRUCTURE": {
        "ALLOWED_ROOT_DIRS": {"02 Areas", "Agents", "Data", "docs", "Experimental", "Projects", "Shared", "Skills", "Workspace"},
        "ALLOWED_ROOT_FILES": {"GEMINI.md", "README.md", "requirements.txt", "settings.json", "main.py", ".gitignore"},
    },
    "DOCUMENTATION": {
        "FULL_TIER_FILES": {"SPECS.md", "TASKS.md", "LOG.md", "DECISIONS.md"},
        "LITE_TIER_TYPE": "lite",
        "MANIFEST_FILENAME": "GEMINI.md",
        "SKILL_MANIFEST_FILENAME": "SKILL.md"
    },
    "PLANNING": {
        "DRAFT_DIR": "Workspace/Strategy",
        "ACTIVE_DIRS": {
            "planerad": "Workspace/Plans/Planerade",
            "pågående": "Workspace/Plans/Pågående"
        },
        "ARCHIVE_DIRS": {
            "slutförd": "Workspace/Archive/Plans/Slutförda",
            "avbruten": "Workspace/Archive/Plans/Avbrutna"
        },
        "REQUIRED_YAML_FIELDS": {"id", "title", "status", "created", "updated", "version"},
        "VALID_STATUSES": {"utkast", "planerad", "pågående", "slutförd", "avbruten"},
        "VALID_PRIORITIES": {"låg", "medel", "hög"},
        "RECOMMENDED_TAGS": {"major", "minor", "patch", "feature", "fix", "core"}
    }
}

def is_ignored(path, root_dir):
    """Checks if a path should be ignored by the librarian."""
    ignore_file = os.path.join(root_dir, ".librarian_ignore")
    ignore_list = {".git", ".venv", "__pycache__", "node_modules", ".gemini"}
    
    if os.path.exists(ignore_file):
        with open(ignore_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    ignore_list.add(line)
    
    parts = os.path.normpath(path).split(os.sep)
    return any(part in ignore_list for part in parts)
