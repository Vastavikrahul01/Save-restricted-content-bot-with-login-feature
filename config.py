import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6437097765:AAF1eUSi1m-X3Mij64_R87ygI_KtEO62fm4")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28590119"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2494557bf21e6c5152f26070aa1a97c7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ps705112:rahul@cluster0.td75ayj.mongodb.net/?retryWrites=true&w=majority")
