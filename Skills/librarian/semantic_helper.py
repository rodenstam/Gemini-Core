import sqlite3
import json
import os
import math
from pathlib import Path

class SemanticHelper:
    def __init__(self, root_dir):
        self.root = Path(root_dir)
        self.db_path = self.root / "Data" / "semantic_index.db"
        # We might need to import Embedder if we want to embed NEW files for comparison
        # But for Phase 3, we focus on files ALREADY in the index.

    def _cosine_similarity(self, v1, v2):
        if not v1 or not v2 or len(v1) != len(v2):
            return 0.0
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude1 = math.sqrt(sum(a * a for a in v1))
        magnitude2 = math.sqrt(sum(b * b for b in v2))
        return dot_product / (magnitude1 * magnitude2) if magnitude1 * magnitude2 > 0 else 0.0

    def get_best_home(self, file_rel_path, top_n=3):
        """
        Uses the vector of the file and compares it against 
        project descriptions (GEMINI.md files) to suggest a home.
        """
        if not self.db_path.exists():
            return None

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 1. Get the vector of our target file
        cursor.execute("SELECT e.vector FROM files f JOIN embeddings e ON f.id = e.file_id WHERE f.path = ?", (file_rel_path,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None # File not indexed yet
        
        target_vector = json.loads(row[0])

        # 2. Get vectors of all GEMINI.md files (project manifests)
        cursor.execute("SELECT f.path, e.vector FROM files f JOIN embeddings e ON f.id = e.file_id WHERE f.path LIKE '%GEMINI.md'")
        manifests = cursor.fetchall()
        
        suggestions = []
        for path, vec_json in manifests:
            # Skip the core GEMINI.md
            if path == "GEMINI.md": continue
            
            vec = json.loads(vec_json)
            score = self._cosine_similarity(target_vector, vec)
            
            # The "home" is the directory containing the manifest
            home_dir = os.path.dirname(path)
            suggestions.append({"home": home_dir, "score": score})

        conn.close()
        suggestions.sort(key=lambda x: x["score"], reverse=True)
        return suggestions[:top_n]
