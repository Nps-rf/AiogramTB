from aiogram import types, Dispatcher
from Maintenance.Buttons import Buttons, Inline_Location, Order_food


async def start_message(message: types.Message):
    await message.answer(text='Добро пожаловать!', reply_markup=Buttons, disable_notification=True)


async def reply_commands(message: types.Message):
    if message.text[1:] == 'Меню':
        await Food.send_food(message)
    elif message.text[1:] == 'Расположение':
        await message.answer('Как удобнее?', reply_markup=Inline_Location)
    elif message.text[1:] == 'Режим работы':
        await send_work_time(message)
    elif message.text[1:] == 'О нас':
        await send_about(message)
    else:
        await message.reply('Ой, я не совсем понял вас(', disable_notification=True,)


async def send_location_map(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer_location(
        latitude=55.753785,
        longitude=37.620540,
        reply_markup=Inline_Location,
        disable_notification=True
    )


async def send_location_adr(query: types.CallbackQuery):
    await query.message.delete()
    await query.message.answer(text='_Москва, Красная площадь_',
                               reply_markup=Inline_Location,
                               disable_notification=True,
                               parse_mode='markdown')


class Food:
    # noinspection SpellCheckingInspection
    photo = open("Food/Khachapuri.jpg", 'rb')

    @classmethod
    async def send_food(cls, message: types.Message):
        caption = '*Хачапури по-имеретински 389р*\n*Вес, гр:* `500`\n' \
                  '*Состав продукта: * `Мука пшеничная, сулугуни, имеретинский сыр, дрожжи, яйцо куриное, ' \
                  'масло сливочное,' ' маргарин, молоко, соль, сахар, масло растительное, вода`'
        await message.answer_photo(photo=cls.photo,
                                   caption=caption,
                                   parse_mode='markdown',
                                   disable_notification=True,
                                   reply_markup=Order_food)


async def send_work_time(message: types.Message):
    await message.answer('Мы работаем с *09:00* до *22:00*', disable_notification=True, parse_mode='markdown')


async def send_about(message: types.Message):
    await message.answer('Здесь расположена информация о нас)', disable_notification=True)


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
    dp.register_message_handler(callback=reply_commands)
    dp.register_callback_query_handler(callback=send_location_map, text='Inline_Location_map')
    dp.register_callback_query_handler(callback=send_location_adr, text='Inline_Location_adr')
