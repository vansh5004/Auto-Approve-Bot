from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21956488"))
    API_HASH = getenv("API_HASH", "812529f879f06436925c7d62eb49f5d1")
    BOT_TOKEN = getenv("BOT_TOKEN", "6908137988:AAFTgMPgWlhnoYy7CD7k_dBQWzjiecgSc50")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001834715749"))
    SUDO = list(map(int, getenv("2020224264").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://APPROVE_BOT:APPROVE_BOT@cluster0.djp96dv.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
