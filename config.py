import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29994788")) #optional
API_HASH = getenv("API_HASH", "fde39a82c05d1ea6aba52b4b36b2e205") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8180921337").split()))
OWNER_ID = int(getenv("6219473300"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("", "8088535693:AAFgDUcsJDWObEwmcuaTvmdJgY8Lhvco6aI")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://graph.org/file/889eb69b32f94476bc712-9558bff09cbd6faaf6.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/TEAMPURVI/ALPHA_USERBOT")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
