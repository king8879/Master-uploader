import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7831273517:AAFzPxGPOGfojuFJg3R67Locjfz12QyWJXI")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "22923037"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6554343173").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
