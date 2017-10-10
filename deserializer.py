#-*- coding: utf-8 -*-

from functools import wraps
import json

def Deserializer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.loads(res)

    return wrapper