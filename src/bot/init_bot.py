from aiogram import Bot
from aiogram.enums import ParseMode
from src.common.config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)  # Initializing the Bot
