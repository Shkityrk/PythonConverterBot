import redis.asyncio as redis

from src.common.config import REDIS_HOST, REDIS_PORT

__all__ = [
    "RedisRepository"
]


class RedisRepository:
    _con: redis.Redis

    async def __aenter__(self) -> "RedisRepository":
        self._con = redis.Redis(
            port=REDIS_PORT,
            host=REDIS_HOST,
            decode_responses=True
        )

        return self

    async def __aexit__(self, exc_type, *_) -> None:
        await self._con.aclose()

    async def set_key(self, key: str, time: int, value: int) -> None:
        await self._con.setex(name=key, time=time, value=value)

    async def get_by_key(self, key: str) -> int | None:
        value = await self._con.get(key)
        return int(value) if value is not None else None

    async def increment_key(self, key: str) -> None:
        await self._con.incr(key)
