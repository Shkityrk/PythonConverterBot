from aiogram import Router, F
from aiogram.types import Message

from src.bot.root import RootRouter
from src.common.config import CHECK_TIME_OUT
from src.bot.root.middlewares import CheckTimeoutMiddleware

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
    await message.answer_photo(message.photo[0].file_id)
