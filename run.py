from aiogram import Bot, Dispatcher
import asyncio
import os
from ai.handlers import router


async def main():
    bot = Bot(token=os.environ["TELEGRAM_BOT_TOKEN"].strip())
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())