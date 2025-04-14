import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7690060051:AAHJOn2nJkmDBXqQCLLQLuJ1Y8ZkkOaiF1Y")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "26468828"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "4693513c08d1ac6af15f95b116c29478")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7517045929").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
