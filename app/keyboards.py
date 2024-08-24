from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


'''main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')], # 1 уровень кнопок
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')] # Второй уровень кнопок
],
                          resize_keyboard=True, #меняеться до минимального размера
                          input_field_placeholder='Выберите пункт меню')
'''
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
    InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])


settings = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Youtube', url='https://youtube.com')]
])

cars =['Жигули', 'BMW', 'Renault']

async def inline_cars():
    #keyboard= ReplyKeyboardBuilder()
    keyboard= InlineKeyboardBuilder()
    for car in cars:
        #keyboard.add(KeyboardButton(text=car))
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return keyboard.adjust(2).as_markup()