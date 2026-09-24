# ALONE-CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "17596251"))
        self.API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8800142370:AAHJQRb8VXhBZFj8OuboaLJ2A6KsIYeLUcg")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1004318913888"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8841848847"))
        
        self.SESSION1 = getenv("SESSION", "BQC86fAAJm427hu3JSzjEVV9dGAJiw5JIFH0b7atzsnD0BTawqyeXbJyhNhePXwufBfyU1AQskaIdNPNM7-1ZuI01OO-J27wS13lxrmijdrFaxQPa0qLzTGkY91K2fEqNRQE3kD7XD_sJG72Wvx7BlEiVEp3ZwrZKsJFw9Ftotu6YWmCB7N8Q2nHAWwRRsrZA75AW0L7OKVFfQVBXjXjz_WazYpWwu9i2kNZG3pZ1PAN2Mw7rJQzaQg_vTzYXJLBJJX-EPqapHlFqG4vol4cbbxOfOgGqB2Jt02I6LpGsT9T4s7tsqnke2Bs426wqF1SGwSTUmlBAyqrY_HvNA1601rx_I58zwAAAAIYbOvjAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneUpdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AloneBotSupport")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
