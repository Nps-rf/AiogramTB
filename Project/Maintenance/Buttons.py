from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# KEYBOARDS
Work_time_b = KeyboardButton(text='🕒Режим работы')
Menu_b = KeyboardButton(text='🍴Меню')
Location_b = KeyboardButton(text='👣Расположение')
About_b = KeyboardButton(text='🥂О нас')
b_list = [Menu_b, Work_time_b, Location_b, About_b]


Buttons = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

for button in b_list:
    Buttons.insert(button)

# INLINES
Inline_Location = InlineKeyboardMarkup(row_width=2, inline_keyboard=True)
Inline_Location_adr = InlineKeyboardButton(text='Адрес', callback_data='Inline_Location_adr')
Inline_Location_map = InlineKeyboardButton(text='На карте', callback_data='Inline_Location_map')

Inline_Location.add(Inline_Location_adr).add(Inline_Location_map)

