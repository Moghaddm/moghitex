import requests
from django.shortcuts import render
from rest_framework.views import APIView
from exchanges.api.api_client import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.telegram.channel_handler import send_message_telegram_channel
from moghitex.settings import TELEGRAM_CHANNEL_ID, TELEGRAM_BOT_TOKEN
from rest_framework import status


# Create your views here.


class CurrencyAPIView(APIView):
    def get(self, request):
        return Response()


@api_view(['POST'])
def send_btc_currencies(request):
    nobitex = get_nobitex_data()
    huluex = get_huluex_data()
    btc = get_btc_data()
    wallex = get_wallex_data()
    tabdeal = get_tabdeal_data()

    message = (f'BTC price: {btc} \n'
               f'nobitext: buy={nobitex['buy']} sell={nobitex['sell']} \n'
               f'huluex: buy={huluex['buy']} sell={nobitex['buy']} \n'
               f'wallex: buy={wallex['buy']} sell={wallex['sell']} \n'
               f'tebdeal: buy={tabdeal['buy']} sell={tabdeal['sell']}')

    response = send_message_telegram_channel(message)
    return response
