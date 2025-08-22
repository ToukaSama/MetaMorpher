#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "22606849")
API_HASH = os.environ.get("API_HASH", "ef85493cd32eadcb5309b5957d8d1b86")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN",'6440021089'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "Hindi_Kochikame")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://meow:meow@meow.a6bo1.mongodb.net/?retryWrites=true&w=majority&appName=meow")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Appraisal")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002310304236')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '6469754522'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1002134572304)
