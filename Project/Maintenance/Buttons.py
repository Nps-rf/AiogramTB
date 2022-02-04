from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
