from aiogram import Bot, Dispatcher
import asyncio
from config import TG_TOKEN

from ai.handlers import router


async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())