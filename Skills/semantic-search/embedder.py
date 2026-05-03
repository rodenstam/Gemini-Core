import requests
import json

class Embedder:
    def __init__(self, api_key, model="gemini-embedding-2"):
        self.api_key = api_key
        self.model = model
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:embedContent?key={api_key}"

    def get_embedding(self, text):
        """Generates a vector embedding for the given text."""
        payload = {
            "model": f"models/{self.model}",
            "content": {
                "parts": [{"text": text}]
            }
        }
        
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            data = response.json()
            
            if 'embedding' in data:
                return data['embedding']['values']
            return None
        except Exception as e:
            print(f"Fel vid embedding: {e}")
            return None

if __name__ == "__main__":
    from credentials_loader import load_gemini_keys
    keys = load_gemini_keys()
    if keys["FREE"]:
        e = Embedder(keys["FREE"])
        vec = e.get_embedding("Detta är ett test.")
        if vec:
            print(f"Embedding genererad (längd: {len(vec)})")
        else:
            print("Misslyckades.")
    else:
        print("Ingen API-nyckel hittades.")
