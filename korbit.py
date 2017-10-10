#-*- coding: utf-8 -*-

from korbit.restapi import RestApi
from korbit.deserializer import Deserializer
from korbit.enums import Currency
from korbit.enums import Method
from korbit.enums import Time
import json
import urllib.parse

class Korbit():
    def __init__(self):
        self.api = RestApi('api.korbit.co.kr')
        self.__nonce = 0

    @property
    def nonce(self):
        self.__nonce += 1
        return self.__nonce

    # 인증
    @Deserializer
    def GetAccessToken(self, client_id, client_secret, email, password):
        params = urllib.parse.urlencode({
            'client_id': client_id,
            'client_secret': client_secret,
            'username': email,
            'password': password,
            'grant_type': 'password'
        })
        headers = {
            'content-type': "application/x-www-form-urlencoded"
        }
        return self.api.request('/v1/oauth2/access_token', Method.POST, payload=params, headers=headers) 

    # Access Token 갱신
    @Deserializer
    def RefreshToken(self, client_id, client_secret, refresh_token):
        params = urllib.parse.urlencode({
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        })
        headers = {
            'content-type': "application/x-www-form-urlencoded"
        }
        return self.api.request('/v1/oauth2/access_token', Method.POST, payload=params, headers=headers) 

    # 사용자 정보 가져오기
    @Deserializer
    def GetUserInfo(self, access_token):
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }
        return self.api.request('/v1/user/info', Method.GET, headers=headers) 

    # 최종 체결 가격
    @Deserializer
    def GetPrice(self, currency=Currency.BTC):
        return self.api.request('/v1/ticker?currency_pair={}'.format(currency.value), Method.GET)

    # 시장 현황 상세정보
    @Deserializer
    def GetDetail(self, currency=Currency.BTC):
        return self.api.request('/v1/ticker/detailed?currency_pair={}'.format(currency.value), Method.GET)

    # 매수/매도 호가
    @Deserializer
    def GetOrderbook(self, currency=Currency.BTC):
        return self.api.request('/v1/orderbook?currency_pair={}'.format(currency.value), Method.GET)

    # 체결 내역
    @Deserializer
    def GetTransactions(self, currency=Currency.BTC, time=Time.HOUR):
        return self.api.request('/v1/transactions?currency_pair={}&time={}'.format(currency.value, Time.HOUR.value), Method.GET)

    # 각종 제약조건
    @Deserializer
    def GetConstants(self):
        return self.api.request('/v1/constants', Method.GET)

    # 매수 주문
    def OrderBuy(self, access_token, payload):
        params = urllib.parse.urlencode(payload)
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'Authorization': 'Bearer {}'.format(access_token)
        }
        print(params)
        print(headers)
        return self.api.request('/v1/user/orders/buy', Method.POST, payload=params, headers=headers)

    # 지정가 주문
    @classmethod
    def OrderBuyLimitTypeParameterBuilder(self, currency, price, coin_amount):
        return {
            'currency_pair': currency.value,
            'type': 'limit',
            'price': price,
            'coin_amount': coin_amount,
            'nonce': self.nonce
        }

    # 시장가 주문
    @classmethod
    def OrderBuyMarketTypeParameterBuilder(self, currency, flat_amount):
        return {
            'currency_pair': currency.value,
            'type': 'market',
            'flat_amount': flat_amount
        }
