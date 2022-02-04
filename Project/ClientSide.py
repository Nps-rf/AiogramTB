from aiogram import types, Dispatcher
from Maintenance.Buttons import Buttons


async def start_message(message: types.Message):
    await message.answer(text='Добро пожаловать!', reply_markup=Buttons)
    await message.delete()


async def reply_commands(message: types.Message):
    if message.text[1:] == 'Меню':
        await send_menu(message)
    elif message.text[1:] == 'Расположение':
        await send_location(message)
    elif message.text[1:] == 'Режим работы':
        await send_work_time(message)
    elif message.text[1:] == 'О нас':
        await send_about(message)


async def send_location(message: types.Message):
    await message.answer('Расположение')


async def send_work_time(message: types.Message):
    await message.answer('09:00-22:00')


async def send_menu(message: types.Message):
    await message.answer('Меню')


async def send_about(message: types.Message):
    await message.answer('О нас')


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
    dp.register_message_handler(callback=reply_commands)
