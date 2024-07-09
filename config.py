import os


class Config(object):
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ.get("TELEGRAM_API")
    OWNER = os.environ.get("OWNER")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    API = environ.get("API", "") # shortlink api
    URL = environ.get("URL", "") # shortlink domain without https://
    VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 
    BOT_USERNAME = environ.get("BOT_USERNAME", "") # bot username without @
    VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
