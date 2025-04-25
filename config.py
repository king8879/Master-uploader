import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7994904406:AAEmKvtbSe4b3UINDxWQqqnq3GE-puYpuv8")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "18579024"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "124981da628d86e21ee492da77cd4037")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "574224129").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "http://master-api-v3.vercel.app")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
