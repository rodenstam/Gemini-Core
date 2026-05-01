import sys
import os

# Lägg till Shared-mappen relativt till detta skript
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_path = os.path.abspath(os.path.join(script_dir, "..", "..", "Shared"))
if shared_path not in sys.path:
    sys.path.append(shared_path)

import gdrive_helper

def search_files(name_query):
    service = gdrive_helper.get_drive_service()
    query = f"name contains '{name_query}' and trashed = false"
    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType, parents, webViewLink)"
    ).execute()
    items = results.get('files', [])
    print(f"\nSearch results for: {query}")
    for item in items:
        parents = item.get('parents', ['No parent'])
        print(f" - {item['name']} ({item['id']}) in {parents}")
        print(f"   Link: {item.get('webViewLink')}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_files(sys.argv[1])
    else:
        search_files("På väg")
        search_files("Svedala")
