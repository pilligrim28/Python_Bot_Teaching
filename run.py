import asyncio
import logging
from aiogram import Bot, Dispatcher


from config import TOKEN #Импортирование токена с файла
from app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) #логирование  для дебаггинга
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
