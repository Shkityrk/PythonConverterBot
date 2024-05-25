from loguru import logger
import redis.asyncio as redis

from src.app_config.config import REDIS_HOST, REDIS_PORT

__all__ = [
    "RedisRepository"
]


class RedisRepository:
    _con: redis.Redis

    async def __aenter__(self) -> "RedisRepository":
        self._con = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

        return self

    async def __aexit__(self, exc_type, *_) -> None:
        if exc_type is not None:
            logger.error(exc_type)

        await self._con.close()
