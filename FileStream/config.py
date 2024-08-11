from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = 5540967#int(env.get("API_ID"))
    API_HASH = "eedf0196b0533f361b51b5b7082358e9"#str(env.get("API_HASH"))
    BOT_TOKEN = "6030145995:AAGqawj9tdp6rAv6FSM6NonH6dbjKBX6rVc" #str(env.get("BOT_TOKEN"))
    OWNER_ID = 1086048529#int(env.get('OWNER_ID', '7978482443'))
    WORKERS = 10 #int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = "mongodb+srv://tej2leecher:aAnJNxbrhK7BHLIN@cachekeys.z4afwu7.mongodb.net/CacheKeys?retryWrites=true&w=majority" #str(env.get('DATABASE_URL'))
    UPDATES_CHANNEL = "TeleXMovieZ"#str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME ="tnstreambot" #str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = True #env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = True
    FLOG_CHANNEL = "-1002184628163"#int(env.get("FLOG_CHANNEL", None))   # Logs channel for file logs
    ULOG_CHANNEL = "-1002184628163" #int(env.get("ULOG_CHANNEL", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = "tzstreamingbot-2e4575a581fe.herokuapp.com"#str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



