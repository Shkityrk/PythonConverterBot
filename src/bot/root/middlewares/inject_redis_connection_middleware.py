from collections.abc import Awaitable, Callable
from typing import Any, TypeAlias

import redis.asyncio as redis
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from loguru import logger

from src.common.config import REDIS_HOST, REDIS_PORT

EventType: TypeAlias = Message | CallbackQuery
HandlerType: TypeAlias = Callable[[EventType, dict[str, Any]], Awaitable[Any]]

__all__ = [
    "InjectRedisConnectionMiddleware",
]


class InjectRedisConnectionMiddleware(BaseMiddleware):
    """Middleware that injects redis connection to data dict"""
    async def __call__(
        self,
        handler: HandlerType,
        event: EventType,
        data: dict[str, Any],
    ) -> Any:
        con = redis.Redis(
            port=REDIS_PORT,
            host=REDIS_HOST,
            decode_responses=True
        )

        logger.debug(f"Injecting redis")
        data["redis_con"] = con
        return await handler(event, data)
