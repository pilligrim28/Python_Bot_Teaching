from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')], # 1 уровень кнопок
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')] # Второй уровень кнопок
],
                          resize_keyboard=True, #меняеться до минимального размера
                          input_field_placeholder='Выберите пункт меню')
