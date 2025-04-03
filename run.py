import asyncio
from aiogram import Bot, Dispatcher
from decouple import config

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()

# dp.include_router

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except: KeyboardInterrupt('Bot Stopped by User')