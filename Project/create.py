from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from Security.TOKEN import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
