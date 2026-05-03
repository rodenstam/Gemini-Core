import requests
import json
import time

class Summarizer:
    def __init__(self, api_key, model="gemini-3.1-flash-lite-preview"):
        self.api_key = api_key
        self.model = model
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    def summarize(self, file_path, content):
        """Generates a brief 2-3 sentence summary of the file content."""
        prompt = f"""
        Analysera följande fil ({file_path}) och ge en kort sammanfattning på 2-3 meningar.
        Fokusera på filens syfte och dess roll i systemet.
        
        INNEHÅLL:
        {content[:4000]} 
        """
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": 150,
                "temperature": 0.2
            }
        }
        
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            data = response.json()
            
            if 'candidates' in data and len(data['candidates']) > 0:
                summary = data['candidates'][0]['content']['parts'][0]['text'].strip()
                return summary
            return "Kunde inte generera sammanfattning."
        except Exception as e:
            return f"Fel vid sammanfattning: {str(e)}"

if __name__ == "__main__":
    from credentials_loader import load_gemini_keys
    keys = load_gemini_keys()
    if keys["FREE"]:
        s = Summarizer(keys["FREE"])
        print(s.summarize("test.py", "print('hello world')"))
    else:
        print("Ingen API-nyckel hittades.")
