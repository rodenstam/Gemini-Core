import os

def load_gemini_keys():
    """Loads Gemini API keys from Data/Credentials/gemini_keys.env."""
    keys = {
        "FREE": None,
        "PAID": None
    }
    
    # Path relative to Gemini-Core root
    env_path = os.path.join("Data", "Credentials", "gemini_keys.env")
    
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    parts = line.split("=", 1)
                    key = parts[0].strip()
                    val = parts[1].strip()
                    if key == "GEMINI_FREE_KEY":
                        keys["FREE"] = val
                    elif key == "GEMINI_PAID_KEY":
                        keys["PAID"] = val
    
    return keys

if __name__ == "__main__":
    # Simple test
    k = load_gemini_keys()
    print(f"Free Key found: {bool(k['FREE'])}")
    print(f"Paid Key found: {bool(k['PAID'])}")
