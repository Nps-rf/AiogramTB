from aiogram import types, Dispatcher


async def start_message(message: types.Message):
    await message.answer('Добро пожаловать!')


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
