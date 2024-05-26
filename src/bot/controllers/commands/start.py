from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.bot.root import RootRouter
from src.common.enums import TelegramCommand
from src.bot.resources.templates import START_COMMAND_TEMPLATE


__all__ = [
    "include_start_command_router",
]

start_command_router = Router()


def include_start_command_router(root_router: RootRouter) -> None:
    root_router.include_router(start_command_router)


@start_command_router.message(Command(TelegramCommand.START_COMMAND))
async def start_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer(text=START_COMMAND_TEMPLATE)
