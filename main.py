import asyncio
import logging
import sys,os

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from user import user_login
from admin import admin_login
load_dotenv()

TOKEN = os.getenv("API")
logger = logging.getLogger(__name__)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    user_login(dp)
    admin_login(dp)

    logger.info("Bot ishga tushmoqda...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("bot_errors.log", encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    asyncio.run(main())