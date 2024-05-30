from pathlib import Path
from io import BytesIO

from aiogram import Router, F
from aiogram.types import Message
from PIL import Image

from src.bot.root import RootRouter
from src.common.config import CHECK_TIME_OUT
from src.bot.root.middlewares import CheckTimeoutMiddleware
from src.python_from_image_converter import PythonFromImageConverter
from src.bot.init_bot import bot

__all__ = [
    "include_photo_router",
]


photo_router = Router()
if CHECK_TIME_OUT:
    photo_router.message.middleware(CheckTimeoutMiddleware())


def include_photo_router(root_router: RootRouter) -> None:
    root_router.include_router(photo_router)


@photo_router.message(F.document)
async def photo_python_handler(message: Message) -> None:
    photo_path = (await bot.get_file(message.document.file_id)).file_path
    await bot.download_file(photo_path, "media/photo.png")

    image = Image.open("media/photo.png")

    python_from_image_converter = PythonFromImageConverter(image)
    converted_python_text = python_from_image_converter.convert_image_to_python()

    await message.answer("<b>Текст, распознанный нейросетью:</b>\n\n"+converted_python_text)
