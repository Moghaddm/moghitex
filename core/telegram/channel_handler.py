import requests
from moghitex.settings import TELEGRAM_CHANNEL_ID, TELEGRAM_BOT_TOKEN
from rest_framework.response import Response


def send_message_telegram_channel(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHANNEL_ID}&text={message}"
        return requests.get(url, timeout=5).json()
    except Exception as exception:
        return Response(repr(exception))
