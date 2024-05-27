from typing import Callable, Any, Awaitable

from loguru import logger
from aiogram import BaseMiddleware
from aiogram.types import Message

from src.redis.services import TimeOutService
from src.bot.resources.templates import YOU_TIMED_OUT

__all__ = [
    "CheckTimeoutMiddleware"
]


class CheckTimeoutMiddleware(BaseMiddleware):
    """Middleware that checks that user can send a photo to be converted to code"""
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        user_id = str(event.from_user.id)

        time_out_service = TimeOutService()
        if await time_out_service.is_timed_out(user_id):
            logger.info(f"REQUEST TO CONVERT FROM USER WITH ID {user_id} && USERNAME {event.from_user.username} "
                        f"IS TIMED OUT")
            await event.answer(YOU_TIMED_OUT)
            return

        return await handler(event, data)
