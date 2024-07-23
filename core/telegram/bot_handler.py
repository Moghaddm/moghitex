from moghitex.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID
import telegram
import requests
from rest_framework.response import Response

bot = telegram.Bot(TELEGRAM_BOT_TOKEN)
