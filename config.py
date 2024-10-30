import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26254064")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7581285542:AAFASkPPL7R9mTO_uHC4iuignWs3xMSp2oo") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'AnimeQuestX') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://abidabdullahown10:abidabdullah1425@cluster0.h3iui.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5296584067")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002197279542')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://envs.sh/IZG.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """{0}"""
