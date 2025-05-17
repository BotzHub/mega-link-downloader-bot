import os

class Config:
    # Required Telegram API credentials
    API_ID = int(os.environ.get("API_ID", "123456"))  # Your API_ID from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")  # Your API_HASH from my.telegram.org
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "your_bot_token_here")  # From @BotFather
    
    # Optional Mega.nz credentials (only needed for premium downloads)
    Mega_email = os.environ.get("Mega_email", "")
    Mega_password = os.environ.get("Mega_password", "")
    
    # Bot configuration
    Bot_username = os.environ.get("Bot_username", "@YourBotUsername")  # Include @
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "123456789").split())  # Allowed user IDs
    OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))  # Your Telegram user ID
    
    # Redis configuration
    REDIS_URI = os.environ.get("REDIS_URI", "redis://localhost:6379")
    REDIS_PASS = os.environ.get("REDIS_PASS", "")
