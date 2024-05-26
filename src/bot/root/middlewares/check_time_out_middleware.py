from typing import Callable, Any, Awaitable

from loguru import logger
from aiogram import BaseMiddleware
from aiogram.types import Message

from src.redis.services import TimeOutService

__all__ = [
    "CheckTimeoutMiddleware"
]


class CheckTimeoutMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        user_id = str(event.from_user.id)

        time_out_service = TimeOutService()

        #  Logic of checking time-out

        return await handler(event, data)
