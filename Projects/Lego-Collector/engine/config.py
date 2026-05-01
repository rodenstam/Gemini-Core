import os
from dotenv import load_dotenv

# Laddar .env filen i samma mapp
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

BRICKSET_API_KEY = os.getenv("BRICKSET_API_KEY", "")
BRICKSET_USERNAME = os.getenv("BRICKSET_USERNAME", "")
BRICKSET_PASSWORD = os.getenv("BRICKSET_PASSWORD", "")

# Om man vill spara userHash för att slippa logga in varje gång
BRICKSET_USER_HASH = os.getenv("BRICKSET_USER_HASH", "")

def check_config():
    if not BRICKSET_API_KEY:
        print("Varning: BRICKSET_API_KEY saknas i .env!")
    if not BRICKSET_USERNAME or not BRICKSET_PASSWORD:
        print("Varning: BRICKSET_USERNAME/PASSWORD saknas i .env!")
