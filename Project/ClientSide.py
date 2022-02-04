from aiogram import types, Dispatcher
from Maintenance.Buttons import Buttons, Inline_Location
from create import bot


async def start_message(message: types.Message):
    await message.answer(text='Добро пожаловать!', reply_markup=Buttons)


async def reply_commands(message: types.Message):
    if message.text[1:] == 'Меню':
        await send_menu(message)
    elif message.text[1:] == 'Расположение':
        await message.answer('Как удобнее?', reply_markup=Inline_Location)
    elif message.text[1:] == 'Режим работы':
        await send_work_time(message)
    elif message.text[1:] == 'О нас':
        await send_about(message)


async def send_location_map(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer_location(
        latitude=55.753785,
        longitude=37.620540,
        reply_markup=Inline_Location
    )


async def send_location_adr(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer(text='Москва, Красная площадь', reply_markup=Inline_Location)


async def send_work_time(message: types.Message):
    await message.answer('09:00-22:00')


async def send_menu(message: types.Message):
    await message.answer('Меню')


async def send_about(message: types.Message):
    await message.answer('О нас')


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
    dp.register_message_handler(callback=reply_commands)
    dp.register_callback_query_handler(callback=send_location_map, text='Inline_Location_map')
    dp.register_callback_query_handler(callback=send_location_adr, text='Inline_Location_adr')
