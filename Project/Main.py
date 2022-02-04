import asyncio
import aiogram
from TOKEN import TOKEN


class Bot(object):
    def __init__(self):
        self.__TOKEN = TOKEN
        self.__name = 'Олег'
        self.__login = r'@nps_rf_bot'
        self.__picture = True

    def __str__(self):
        return f'Name: {self.__name} \nlogin: {self.__login} \nHas picture? -> {self.__picture}'
