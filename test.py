#-*- coding: utf-8 -*-

from korbit.restapi import RestApi
from korbit.enums import Method
from korbit.enums import Currency
from korbit.korbit import Korbit
import configparser

# api = RestApi('api.korbit.co.kr')
# result = api.request('/v1/ticker/detailed?currency_pair=eth_krw', Method.GET)
# print(result)

# k = Korbit()
# k.GetPrice()
# k.GetDetail()
# k.GetOrderbook()
# k.GetTransactions()
# k.GetConstants()

# config = configparser.ConfigParser()
# config.read('config.ini')

# client_id = config['OAUTH']['CLIENT_ID']
# client_secret = config['OAUTH']['CLIENT_SECRET']
# email = config['OAUTH']['EMAIL']
# password = config['OAUTH']['PASSWORD']

# token = k.GetAccessToken(client_id, client_secret, email, password)
# access_token = token['access_token']
# user = k.GetUserInfo(access_token)

# payload = Korbit.OrderBuyLimitTypeParameterBuilder(Currency.ETH, 344400, 0.01)
# r = k.OrderBuy(access_token, payload)
