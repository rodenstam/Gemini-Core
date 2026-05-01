import os
import re
import sys

# Lägg till Shared-mappen relativt till detta skript (för framtida bruk)
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_path = os.path.abspath(os.path.join(script_dir, "..", "..", "Shared"))
if shared_path not in sys.path:
    sys.path.append(shared_path)

# Sökvägar till projektmappar i Obsidian-valvet
# Dessa ligger på samma Drive (H:)
TARGET_DIRS = [
    r"h:\My Drive\Obsidian\01 Projects\På väg",
    r"h:\My Drive\Obsidian\01 Projects\Svedalas bostadssociala program",
    r"h:\My Drive\Obsidian\02 Areas\Kreativt skrivande\Sångtexter",
    r"h:\My Drive\Obsidian\02 Areas\Arbetsliv\ansökningar"
]

def cleanup_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Ta bort YAML-metadata (original_url)
    # Matchar --- ... original_url: ... ---
    new_content = re.sub(r'---\s*\n(.*?)\noriginal_url:.*?\n(.*?)---', r'---\n\1\n\2---', content, flags=re.DOTALL)
    # Om det bara var original_url kvar i YAML, rensa ev. tomma rader
    new_content = re.sub(r'---\s*\n\s*\n---', '', new_content)
    
    # 2. Ta bort Digital Tvilling-blocket
    new_content = re.sub(r'> \[!info\] \*\*Digital Tvilling\*\*.*?\n> 🔗 \[.*?\]\(.*?\)\n\n', '', new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def run_cleanup():
    count = 0
    for target_dir in TARGET_DIRS:
        if not os.path.exists(target_dir):
            print(f"Hittade inte mappen: {target_dir}")
            continue
            
        print(f"Städar i: {target_dir}")
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith('.md'):
                    if cleanup_file(os.path.join(root, file)):
                        count += 1
    print(f"Klar! Städade {count} filer.")

if __name__ == "__main__":
    run_cleanup()
