import requests
import json
from credentials_loader import load_gemini_keys

def test_model(model_id):
    keys = load_gemini_keys()
    api_key = keys["FREE"]
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={api_key}"
    
    payload = {
        "contents": [{"parts": [{"text": "Säg hej!"}]}]
    }
    
    print(f"Testar modell: {model_id}...")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ SUCCESS: {model_id} fungerar!")
            return True
        else:
            print(f"❌ FAIL: {model_id} gav status {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    models_to_test = [
        "gemini-3.1-flash-lite",
        "gemini-3.1-flash-lite-preview",
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest"
    ]
    for m in models_to_test:
        test_model(m)
