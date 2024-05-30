from aiogram import Router, F
from aiogram.types import Message
from io import BytesIO
from PIL import Image
from loguru import logger

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


@photo_router.message(F.photo)
async def photo_python_handler(message: Message) -> None:
    bytes_image = BytesIO()
    photo_path = (await bot.get_file(message.photo[0].file_id)).file_path
    await bot.download_file(photo_path, bytes_image)

    image = Image.open(bytes_image)

    python_from_image_converter = PythonFromImageConverter(image)
    converted_python_text = python_from_image_converter.convert_image_to_python()

    logger.info(converted_python_text)

    #await message.answer(converted_python_text)
