from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router=Router()


@router.message(CommandStart()) #ждет комнады старт handler
async def cmd_start(message: Message):
    await message.reply(f'Привет, \nтвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                       reply_markup=await kb.inline_cars())

@router.message(Command('help')) #ждет комнады help handler
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text == 'Как дела?') #Вопрос-ответ
async def how_are_you(message: Message):
    await message.answer('Ok!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMYZsdJ1QvTu_uavkLRFsfFKuG4rkUAAojhMRtHPTlK_Cvcw8CkTSIBAAMCAANtAAM1BA', caption = 'Это запрос Json')

