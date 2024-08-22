import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN #Импортирование токена с файла

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart()) #ждет комнады старт
async def cmd_start(message: Message):
    await message.answer('Привет, Кракозябра')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) #логирование  для дебаггинга
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
