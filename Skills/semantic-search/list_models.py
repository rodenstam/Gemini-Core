import requests
import json
from credentials_loader import load_gemini_keys

def list_models():
    keys = load_gemini_keys()
    api_key = keys["FREE"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_models()
