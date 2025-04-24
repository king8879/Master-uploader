import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7580026996:AAGA6SYg9Zl6NMSnwbYxSAtKMTtEfCTSXz0")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "22528446"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "0d81bf18019c5f3839037d0ae737c358")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "633111330").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
