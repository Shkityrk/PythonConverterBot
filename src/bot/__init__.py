from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.common.config import BOT_TOKEN
from src.bot.root_router import build_root_router

__all__ = [
    "bot",
    "dispatcher"
]

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)  # Initializing the Bot (I guess it's Singleton)

dispatcher = Dispatcher(storage=MemoryStorage())  # Although storage is not used now I hope I'll use it later
dispatcher.include_router(build_root_router())  # Including root router to dispatcher
