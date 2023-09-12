from os import environ

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN")
API_URL = environ.get("API_URL")