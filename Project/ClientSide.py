from aiogram import types, Dispatcher
from Maintenance.Keyboards.buttons import Buttons
from Maintenance.Inlines.buttons import Inline_Location, Order_food, Next_Inline_About
from Others.Text import *


class Statements(object):
    CART = []
    Current_order = None


async def start_message(message: types.Message):
    start_text = '*Добро пожаловать в Имеретию!*'
    await message.answer(text=start_text,
                         reply_markup=Buttons,
                         disable_notification=True,
                         parse_mode='markdown')


async def reply_commands(message: types.Message):
    request = message.text[1:]
    if request == 'Меню':
        await Food.send_khachapuri(message)
    elif request == 'Расположение':
        await message.answer('Как удобнее?', reply_markup=Inline_Location)
    elif request == 'Время работы':
        await send_work_time(message)
    elif request == 'О нас':
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


# noinspection SpellCheckingInspection
class Food(object):
    def __init__(self, ident, name, price, caption, photo_addr): # TODO
        self.ID = ident
        self.name = name
        self.price = price
        self.caption = caption
        self.photo_addr = photo_addr

    Khachapuri_ID = r'001'

    @staticmethod
    async def send_khachapuri(message: types.Message):
        Statements.Current_order = Food.Khachapuri_ID
        caption = "*Хачапури по-имеретински 389р*\n*Вес, гр:* `500`\n" \
                  "*Состав продукта: * `Мука пшеничная, сулугуни, имеретинский сыр, дрожжи, яйцо куриное, " \
                  "масло сливочное," " маргарин, молоко, соль, сахар, масло растительное, вода`"
        with open("Food/Khachapuri.jpg", 'rb') as photo:
            await message.answer_photo(photo=photo,
                                       caption=caption,
                                       parse_mode='markdown',
                                       disable_notification=True,
                                       reply_markup=Order_food)


class Payments(object):
    @staticmethod
    async def add_to_cart(callback: types.CallbackQuery):
        message = callback.message
        Statements.CART.append(Statements.Current_order)
        await message.answer('Добавил')
        await message.answer(Statements.Current_order)


async def send_work_time(message: types.Message):
    await message.answer('Мы работаем с *09:00* до *22:00*', disable_notification=True, parse_mode='markdown')


async def send_about(message: types.Message):
    # noinspection SpellCheckingInspection
    INFO = '🥤`Пекарня Imereti`🥤' \
           '\n*Мы стараемся не придерживаться шаблонов и всегда ищем новые и оригинальные идеи на кухне, ' \
           'чтобы удивлять и радовать вас.*✍️'
    await message.answer(text=INFO, disable_notification=True, parse_mode='markdown', reply_markup=Next_Inline_About)


async def send_more_about(query: types.CallbackQuery):
    fact = next(about)
    await query.message.answer(text=fact,
                               disable_notification=True,
                               parse_mode='markdown',
                               reply_markup=Next_Inline_About if fact != about_list[-1] else None)


def activate_message_handlers(dp: Dispatcher):
    dp.register_message_handler(callback=start_message, commands=('start',))
    dp.register_message_handler(callback=reply_commands)


def register_callback_query_handlers(dp: Dispatcher):
    """
    :param dp:
    :return: None
    query_callbacks =
        1) 'Inline_Location_map' -> show map
        2) 'Inline_Location_adr' -> show address
        3) 'Next_Inline_About_b' -> show more info about us
    """
    dp.register_callback_query_handler(callback=send_location_map, text='Inline_Location_map')
    dp.register_callback_query_handler(callback=send_location_adr, text='Inline_Location_adr')
    dp.register_callback_query_handler(callback=send_more_about, text='Next_Inline_About_b')
    dp.register_callback_query_handler(callback=Payments.add_to_cart, text='Order_food_b')


def activate_handlers(dp: Dispatcher):
    activate_message_handlers(dp)
    register_callback_query_handlers(dp)
