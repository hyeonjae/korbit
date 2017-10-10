#-*- coding: utf-8 -*-

from functools import wraps

def Close(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        args[0].close()
        return res

    return wrapper