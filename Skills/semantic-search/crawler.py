import os
import hashlib
import time
from db_manager import DatabaseManager
from summarizer import Summarizer
from embedder import Embedder
from credentials_loader import load_gemini_keys

class Crawler:
    def __init__(self, root_dir="."):
        self.root_dir = root_dir
        self.db = DatabaseManager()
        keys = load_gemini_keys()
        self.summarizer = Summarizer(keys["FREE"])
        self.embedder = Embedder(keys["FREE"])
        
        # Files to ignore
        self.ignore_dirs = {'.git', '.venv', '__pycache__', 'node_modules', 'Data'}
        self.allowed_extensions = {'.py', '.md', '.txt', '.js', '.json'}

    def _get_file_hash(self, path):
        hasher = hashlib.md5()
        with open(path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def index_all(self, silent=False):
        lock_file = os.path.join("Data", "indexer.lock")
        
        # Check for lock
        if os.path.exists(lock_file):
            if not silent:
                print("--- ⚠️ Indexering pågår redan (lock hittad). Avbryter. ---")
            return

        # Create lock
        try:
            os.makedirs(os.path.dirname(lock_file), exist_ok=True)
            with open(lock_file, "w") as f:
                f.write(str(os.getpid()))

            if not silent:
                print(f"--- 🧠 Startar semantisk indexering av {os.path.abspath(self.root_dir)} ---")
            
            count_indexed = 0
            count_skipped = 0
            
            for root, dirs, files in os.walk(self.root_dir):
                # Pruning ignored directories
                dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
                
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext not in self.allowed_extensions:
                        continue
                    
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.root_dir)
                    
                    try:
                        current_hash = self._get_file_hash(file_path)
                        db_info = self.db.get_file_info(rel_path)
                        
                        if db_info and db_info[1] == current_hash:
                            count_skipped += 1
                            continue
                        
                        if not silent:
                            print(f"Indexing: {rel_path}...")
                        
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        # 1. Summarize (Gemini Flash)
                        summary = self.summarizer.summarize(rel_path, content)
                        if "Fel vid sammanfattning" in summary:
                            if not silent:
                                print(f"Skipping {rel_path} due to summarization error: {summary}")
                            continue
                        
                        # 2. Embed (gemini-embedding-2)
                        # We combine filename and summary for better semantic grounding
                        text_to_embed = f"File: {rel_path}\nSummary: {summary}"
                        vector = self.embedder.get_embedding(text_to_embed)
                        
                        if vector:
                            self.db.update_file(rel_path, current_hash, summary, vector)
                            count_indexed += 1
                            # Rate limit protection for Free Tier (15 RPM -> 4s wait)
                            time.sleep(4) 
                        else:
                            if not silent:
                                print(f"Skipping {rel_path} due to embedding failure.")
                            
                    except Exception as e:
                        if not silent:
                            print(f"Error indexing {rel_path}: {e}")

            if not silent:
                print(f"--- Indexering klar! {count_indexed} nya/uppdaterade, {count_skipped} oförändrade. ---")

        finally:
            # Remove lock
            if os.path.exists(lock_file):
                os.remove(lock_file)

if __name__ == "__main__":
    crawler = Crawler()
    crawler.index_all()
