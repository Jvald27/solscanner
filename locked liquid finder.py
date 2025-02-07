import time
import requests
from solders.pubkey import Pubkey
from solana.rpc.api import Client

# Solana RPC Node (Replace with your own if needed)
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
client = Client(SOLANA_RPC_URL)

# Fake "Locked Liquidity" Smart Contract Address (Replace with real ones)
LOCKED_LIQUIDITY_PROGRAM_IDS = [
    "example_program_1",
    "example_program_2"
]

# Function to fetch recent token launches with error handling
def get_recent_tokens():
    try:
        response = requests.get("https://api.dexscreener.com/latest/dex/tokens/solana", timeout=10)
        response.raise_for_status()  # Raises an error for HTTP issues (4xx, 5xx)
        data = response.json()
        return data.get("pairs", [])  # Ensure it returns an empty list if "pairs" is missing
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        return []  # Return an empty list instead of None

# Function to check if liquidity is locked
def is_liquidity_locked(token_address):
    try:
        token_pubkey = Pubkey(token_address)
        account_info = client.get_account_info(token_pubkey)

        if account_info.value is not None:
            owner = account_info.value.owner
            if owner in LOCKED_LIQUIDITY_PROGRAM_IDS:
                return True
        return False
    except Exception as e:
        print(f"⚠️ Error checking liquidity lock for {token_address}: {e}")
        return False

# Function to monitor token launches every 10 seconds
def monitor_token_launches():
    print("🔍 Scanning for live token launches with locked liquidity (Every 10 seconds)...")
    while True:
        tokens = get_recent_tokens()
        if not tokens:
            print("⚠️ No tokens found or API issue. Retrying in 10 seconds...")
        else:
            for token in tokens:
                token_address = token.get("pairAddress", "N/A")
                if token_address != "N/A" and is_liquidity_locked(token_address):
                    print(f"✅ Locked Liquidity Found: {token['baseToken']['symbol']} ({token_address})")

        time.sleep(10)  # Runs every 10 seconds

if __name__ == "__main__":
    monitor_token_launches()
