from os import getenv

from dotenv import load_dotenv

load_dotenv()
# Mandatory VARS
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
STRING_SESSION = getenv("STRING_SESSION")
VIDEO_CHAT_ID = int(getenv("VIDEO_CHAT_ID"))
