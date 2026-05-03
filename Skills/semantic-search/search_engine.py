import math
from db_manager import DatabaseManager
from embedder import Embedder
from credentials_loader import load_gemini_keys

class SearchEngine:
    def __init__(self):
        self.db = DatabaseManager()
        keys = load_gemini_keys()
        self.embedder = Embedder(keys["FREE"])

    def _cosine_similarity(self, v1, v2):
        """Calculates cosine similarity between two vectors in pure Python."""
        if not v1 or not v2 or len(v1) != len(v2):
            return 0.0
        
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude1 = math.sqrt(sum(a * a for a in v1))
        magnitude2 = math.sqrt(sum(b * b for b in v2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
            
        return dot_product / (magnitude1 * magnitude2)

    def search(self, query, top_n=5):
        """Searches for the most relevant files based on the query."""
        query_vector = self.embedder.get_embedding(query)
        if not query_vector:
            return []

        all_data = self.db.get_all_embeddings()
        results = []
        
        for item in all_data:
            similarity = self._cosine_similarity(query_vector, item["vector"])
            results.append({
                "path": item["path"],
                "summary": item["summary"],
                "score": similarity
            })
            
        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_n]

if __name__ == "__main__":
    engine = SearchEngine()
    query = "Hur hanterar vi Lego-data?"
    res = engine.search(query)
    for r in res:
        print(f"[{r['score']:.4f}] {r['path']}\n   -> {r['summary']}")
