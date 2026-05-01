import os
import io
import json
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Scopes
SCOPES = ['https://www.googleapis.com/auth/drive']
ROBOT_FOLDER_ID = "19g7u7mfZFK-ZPKjvVyGohMaOsubRZRD0"

def get_drive_service():
    creds = None
    base_dir = os.path.dirname(os.path.dirname(__file__))
    token_path = os.path.join(base_dir, "Data", "Credentials", "token.json")
    creds_path = os.path.join(base_dir, "Data", "Credentials", "credentials.json")

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def find_file_id_in_robot_folder(file_name):
    """Söker efter en fil med specifikt namn på Drive."""
    service = get_drive_service()
    # Hantera apostrofer i filnamnet genom att escapea dem
    safe_name = file_name.replace("'", "\\'")
    query = f"name = '{safe_name}' and mimeType = 'application/vnd.google-apps.document' and trashed = false"
    results = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    items = results.get('files', [])
    return items[0]['id'] if items else None

def export_gdoc_to_docx(file_id, output_path):
    """Exporterar ett Google Doc till en lokal .docx-fil."""
    service = get_drive_service()
    request = service.files().export_media(
        fileId=file_id,
        mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    
    with open(output_path, 'wb') as f:
        f.write(fh.getvalue())
    return True
