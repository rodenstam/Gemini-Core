import sys
import os

# Lägg till Shared-mappen relativt till detta skript
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_path = os.path.abspath(os.path.join(script_dir, "..", "..", "Shared"))
if shared_path not in sys.path:
    sys.path.append(shared_path)

import gdrive_helper

def list_recursive(service, folder_id, indent=0):
    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        fields="files(id, name, mimeType)"
    ).execute()
    items = results.get('files', [])
    for item in items:
        print('  ' * indent + f"- {item['name']} ({item['id']}) [{item['mimeType']}]")
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            list_recursive(service, item['id'], indent + 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_id = sys.argv[1]
    else:
        print("Usage: python list_folder.py <folder_id>")
        sys.exit(1)
    service = gdrive_helper.get_drive_service()
    list_recursive(service, folder_id)
