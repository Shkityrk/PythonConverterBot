from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.app_config.config import BOT_TOKEN

__all__ = [
    "bot",
    "dispatcher"
]

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

dispatcher = Dispatcher(storage=MemoryStorage())
