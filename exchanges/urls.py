from django.urls import path
from exchanges.views import get_nobitex_data
from exchanges.views import CurrencyAPIView, send_message_telegram_channel

urlpatterns = [
    path('send-message/', send_message_telegram_channel, name='send_message_telegram_channel')
]
