import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN #Импортирование токена с файла

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart()) #ждет комнады старт handler
async def cmd_start(message: Message):
    await message.answer('Привет, Кракозябра')

@dp.message(Command('help')) #ждет комнады help handler
async def get_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(F.text == 'Как дела?') #Вопрос ответ
async def how_are_you(message: Message):
    await message.answer('Ok!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) #логирование  для дебаггинга
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
