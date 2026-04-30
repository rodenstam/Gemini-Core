import os
import subprocess
import sys
import shutil
import re
import io
from googleapiclient.http import MediaIoBaseDownload

# Lägg till sökväg för att kunna importera gdrive_helper
sys.path.append(os.path.dirname(__file__))
import gdrive_helper

def clean_markdown(md_content, gdoc_url=None):
    """Städar Pandoc-output och lägger till digital tvilling-länk."""
    lines = md_content.split('\n')
    new_lines = []
    skip_toc = False
    
    for line in lines:
        if line.strip().lower().startswith('# innehåll') or line.strip().lower().startswith('# table of contents'):
            skip_toc = True
            continue
        if skip_toc:
            if re.match(r'^\s*\[.*\]\(#.*\)\s*$', line) or not line.strip():
                continue
            else:
                skip_toc = False
        new_lines.append(line)
    
    content = '\n'.join(new_lines)
    content = content.replace('\\"', '"')
    
    header = "---\ntype: imported_document\n"
    if gdoc_url:
        header += f"original_url: {gdoc_url}\n"
    header += "---\n\n"
    
    if gdoc_url:
        header += f"> [!info] **Digital Tvilling**\n> 🔗 [Redigera originalet i Google Drive]({gdoc_url})\n\n"
        
    return header + content

def convert_to_md(docx_path, md_path, gdoc_url=None):
    """Konverterar DOCX till städad Markdown."""
    try:
        subprocess.run(['pandoc', docx_path, '-o', md_path, '--markdown-headings=atx'], check=True)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        cleaned_content = clean_markdown(content, gdoc_url)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        return True
    except Exception as e:
        print(f"Error converting {docx_path}: {e}")
        return False

def download_file(service, file_id, output_path):
    """Laddar ner en binär fil från Drive."""
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    with open(output_path, 'wb') as f:
        f.write(fh.getvalue())

def import_drive_file(service, item, target_path, originals_dir):
    """Hanterar hela processen för en enskild fil."""
    file_name = item['name']
    file_id = item['id']
    mime_type = item['mimeType']
    url = item.get('webViewLink')
    
    safe_name = name_to_safe(file_name)
    archive_docx = os.path.join(originals_dir, safe_name + ".docx")
    
    if mime_type == 'application/vnd.google-apps.document':
        if gdrive_helper.export_gdoc_to_docx(file_id, archive_docx):
            return convert_to_md(archive_docx, target_path, url)
    elif mime_type.endswith('wordprocessingml.document') or file_name.endswith('.docx') or mime_type == 'application/rtf' or file_name.endswith('.rtf'):
        # För RTF och DOCX, ladda ner originalet först
        ext = ".docx" if "word" in mime_type or file_name.endswith('.docx') else ".rtf"
        archive_path = os.path.join(originals_dir, safe_name + ext)
        download_file(service, file_id, archive_path)
        return convert_to_md(archive_path, target_path, url)
    elif mime_type == 'text/markdown' or file_name.endswith('.md'):
        request = service.files().get_media(fileId=file_id)
        with open(target_path, 'wb') as f:
            f.write(request.execute())
        # Städa även befintlig MD
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(clean_markdown(content, url))
        return True
    return False

def name_to_safe(name):
    """Skapar ett säkert filnamn."""
    safe = name.replace(':', ' ').replace('.docx', '').replace('.md', '').strip()
    return "".join([c for c in safe if c.isalnum() or c in (' ', '.', '_')]).strip()
