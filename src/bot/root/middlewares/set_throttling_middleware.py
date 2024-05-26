from collections.abc import Awaitable, Callable
from typing import Any, TypeAlias

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.flags import get_flag
from loguru import logger

from src.redis.services import ThrottlingService

EventType: TypeAlias = Message | CallbackQuery
HandlerType: TypeAlias = Callable[[EventType, dict[str, Any]], Awaitable[Any]]

__all__ = [
    "SetThrottlingMiddleware",
]


class SetThrottlingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: HandlerType,
        event: EventType,
        data: dict[str, Any],
    ) -> Any:
        user_id = str(event.from_user.id)

        if get_flag(data, "void_command"):
            logger.info("VOID COMMAND NOT THROTTLED")
            return

        throttling_service = ThrottlingService()

        #  Logic of throttling...

        return await handler(event, data)
