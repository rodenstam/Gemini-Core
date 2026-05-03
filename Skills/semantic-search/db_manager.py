import sqlite3
import os
import json
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="Data/semantic_index.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Table for file metadata
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                path TEXT UNIQUE,
                hash TEXT,
                summary TEXT,
                last_indexed TEXT
            )
        ''')
        
        # Table for embeddings (stored as JSON for pure-python compatibility)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS embeddings (
                file_id INTEGER PRIMARY KEY,
                vector TEXT,
                FOREIGN KEY (file_id) REFERENCES files (id) ON DELETE CASCADE
            )
        ''')
        
        conn.commit()
        conn.close()

    def get_file_info(self, path):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, hash, summary FROM files WHERE path = ?", (path,))
        result = cursor.fetchone()
        conn.close()
        return result

    def update_file(self, path, file_hash, summary, vector):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            # Insert or replace file info
            cursor.execute('''
                INSERT INTO files (path, hash, summary, last_indexed)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(path) DO UPDATE SET
                    hash = excluded.hash,
                    summary = excluded.summary,
                    last_indexed = excluded.last_indexed
            ''', (path, file_hash, summary, datetime.now().isoformat()))
            
            file_id = cursor.execute("SELECT id FROM files WHERE path = ?", (path,)).fetchone()[0]
            
            # Update embedding
            cursor.execute('''
                INSERT INTO embeddings (file_id, vector)
                VALUES (?, ?)
                ON CONFLICT(file_id) DO UPDATE SET
                    vector = excluded.vector
            ''', (file_id, json.dumps(vector)))
            
            conn.commit()
        finally:
            conn.close()

    def get_all_embeddings(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT f.path, f.summary, e.vector 
            FROM files f 
            JOIN embeddings e ON f.id = e.file_id
        ''')
        results = []
        for path, summary, vector_json in cursor.fetchall():
            results.append({
                "path": path,
                "summary": summary,
                "vector": json.loads(vector_json)
            })
        conn.close()
        return results
