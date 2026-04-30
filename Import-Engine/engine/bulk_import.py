import sys
import os
import io
from googleapiclient.http import MediaIoBaseDownload

# Lägg till Shared-mappen relativt till detta skript
script_dir = os.path.dirname(os.path.abspath(__file__))
shared_path = os.path.abspath(os.path.join(script_dir, "..", "Shared"))
if shared_path not in sys.path:
    sys.path.append(shared_path)

import gdrive_helper
import gdrive_import_tool

def bulk_import(service, folder_id, vault_project_path):
    attachments_dir = os.path.join(vault_project_path, "attachments")
    
    map_mime = {
        "Sources": [
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/msword",
            "application/vnd.google-apps.document"
        ],
        "PDF": ["application/pdf"],
        "Presentations": [
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.google-apps.presentation"
        ],
        "Sheets": [
            "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.google-apps.spreadsheet"
        ],
        "Images": ["image/png", "image/jpeg", "image/gif"]
    }

    def get_target_dir(mime_type):
        for folder, mimes in map_mime.items():
            if mime_type in mimes:
                return os.path.join(attachments_dir, folder)
        return None

    def download_binary(service, file_id, output_path):
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        with open(output_path, 'wb') as f:
            f.write(fh.getvalue())

    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed = false",
        fields="files(id, name, mimeType, webViewLink)"
    ).execute()
    items = results.get('files', [])
    
    for item in items:
        name = item['name']
        mime = item['mimeType']
        file_id = item['id']
        
        if mime == 'application/vnd.google-apps.folder':
            print(f"\n--- Går in i mapp: {name} ---")
            bulk_import(service, file_id, vault_project_path)
            continue
            
        if name.lower() in ['thumbs.db', 'desktop.ini']:
            continue
            
        target_dir = get_target_dir(mime)
        if not target_dir:
            print(f"Skippar okänd typ: {name} ({mime})")
            continue
            
        print(f"Hanterar: {name}")
        
        # Säkert namn
        safe_base = gdrive_import_tool.name_to_safe(name)
        
        if target_dir.endswith("Sources"):
            # Markdown-konvertering
            target_path = os.path.join(target_dir, safe_base + ".md")
            originals_dir = os.path.join(attachments_dir, "Originals")
            gdrive_import_tool.import_drive_file(service, item, target_path, originals_dir)
        else:
            # Binär nedladdning (PDF, PPTX, XLS, Images)
            ext = os.path.splitext(name)[1]
            if not ext:
                if "pdf" in mime: ext = ".pdf"
                elif "presentation" in mime: ext = ".pptx"
                elif "spreadsheet" in mime: ext = ".xlsx"
                elif "image" in mime: ext = ".png"
            
            target_path = os.path.join(target_dir, safe_base + ext)
            
            # Om det är en Google-typ som inte är doc, exportera den
            if mime.startswith('application/vnd.google-apps.'):
                if "presentation" in mime:
                     target_path = os.path.join(target_dir, safe_base + ".pdf")
                     gdrive_helper.export_gdoc_to_pdf(file_id, target_path)
                elif "spreadsheet" in mime:
                     gdrive_helper.export_gdoc_to_xlsx(file_id, target_path)
            else:
                download_binary(service, file_id, target_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bulk_import.py <folder_id> <vault_project_path>")
        print("Example: python bulk_import.py 1jj-X8lKwt-pivh4p8yXAe2MWILeefitl \"h:\\My Drive\\Obsidian\\01 Projects\\På väg\"")
        sys.exit(1)
        
    folder_id = sys.argv[1]
    project_path = sys.argv[2]
    
    service = gdrive_helper.get_drive_service()
    bulk_import(service, folder_id, project_path)

