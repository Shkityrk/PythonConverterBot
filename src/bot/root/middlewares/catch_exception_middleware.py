from collections.abc import Awaitable, Callable
from typing import Any, TypeAlias

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from loguru import logger

EventType: TypeAlias = Message | CallbackQuery
HandlerType: TypeAlias = Callable[[EventType, dict[str, Any]], Awaitable[Any]]

__all__ = [
    "CatchExceptionMiddleware",
]


class CatchExceptionMiddleware(BaseMiddleware):
    """Middleware that catches exceptions and logs them to the log file"""
    async def __call__(
        self,
        handler: HandlerType,
        event: EventType,
        data: dict[str, Any],
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as e:
            logger.exception("EXCEPTION DURING THE PROCESS: " + e.__str__())
