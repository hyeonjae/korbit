#-*- coding: utf-8 -*-

from enum import Enum

class Method(Enum):
    GET = 'GET'
    POST = 'POST'

class Currency(Enum):
    BTC = 'btc_krw'
    ETH = 'eth_krw'
    XRP = 'xrp_krw'

class Time(Enum):
    HOUR = 'hour'
    MINUTE = 'minute'
    DAY = 'day'