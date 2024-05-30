from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.root_router import build_root_router
from src.bot.init_bot import bot

__all__ = [
    "bot",
    "dispatcher"
]

dispatcher = Dispatcher(storage=MemoryStorage())  # Although storage is not used now I hope I'll use it later
dispatcher.include_router(build_root_router())  # Including root router to dispatcher
