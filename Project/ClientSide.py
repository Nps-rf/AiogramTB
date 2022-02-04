from aiogram import types, Dispatcher
from Maintenance.Buttons import Buttons


async def start_message(message: types.Message):
    await message.answer(text='Добро пожаловать!', reply_markup=Buttons)
    await message.delete()


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
