import logging
from distutils.util import strtobool
from logging.handlers import RotatingFileHandler

# 🔐 CONFIG UTAMA
TG_BOT_TOKEN = "8635273696:AAENB8pad3OdVx8B33b1L32xMT77WVAZ7Vw"
APP_ID = 35019041
API_HASH = "131c3a26243bbd2e6c67fac16df78a72"

CHANNEL_ID = -1003984464579
OWNER = "@reformasitotal"

ADMINS = [6860872910]

FORCE_SUB_CHANNEL = -1003439226924

# ⚙️ SETTINGS
PROTECT_CONTENT = False
TG_BOT_WORKERS = 4

START_MSG = "<b>Halo {first} 👋\n\nanjing kamu 🔥</b>"
FORCE_MSG = "<b>⚠️ Join channel dulu bro!</b>"

CUSTOM_CAPTION = None
DISABLE_CHANNEL_BUTTON = False

# 🧾 LOG
LOG_FILE_NAME = "logs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=5),
        logging.StreamHandler(),
    ],
)

def LOGGER(name: str):
    return logging.getLogger(name)
