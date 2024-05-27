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
    """Middleware to throttle events from noisy users"""
    async def __call__(
        self,
        handler: HandlerType,
        event: EventType,
        data: dict[str, Any],
    ) -> Any:
        user_id = str(event.from_user.id)
        redis_con = data["redis_con"]

        if get_flag(data, "void_command"): return

        throttling_service = ThrottlingService(redis_con)
        if await throttling_service.need_to_throttle(user_id):
            logger.info(f"MESSAGE FROM USER WITH ID {user_id} && USERNAME {event.from_user.username} WAS THROTTLED")
            return

        return await handler(event, data)
