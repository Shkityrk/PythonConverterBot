from aiogram import Router, F
from aiogram.types import Message

from src.bot.root import RootRouter
from src.bot.resources.templates import CONVERTED_TEXT_TEMPLATE
from src.common.config import CHECK_TIME_OUT
from src.common.utils import download_image_from_telegram
from src.bot.root.middlewares import CheckTimeoutMiddleware
from src.python_from_image_converter import PythonFromImageConverter

__all__ = [
    "include_covert_image_router",
]


convert_image_router = Router()
if CHECK_TIME_OUT:
    convert_image_router.message.middleware(CheckTimeoutMiddleware())


def include_covert_image_router(root_router: RootRouter) -> None:
    root_router.include_router(convert_image_router)


@convert_image_router.message(F.document)
async def photo_python_handler(message: Message) -> None:
    image = await download_image_from_telegram(message.document.file_id)
    python_from_image_converter = PythonFromImageConverter(image)
    converted_python_text = python_from_image_converter.convert_image_to_python()

    await message.answer(CONVERTED_TEXT_TEMPLATE+converted_python_text)
