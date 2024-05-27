import redis.asyncio as redis


__all__ = [
    "RedisRepository"
]


class RedisRepository:
    _con: redis.Redis

    def __init__(self, redis_con: redis.Redis) -> None:
        self._con = redis_con

    async def __aenter__(self) -> "RedisRepository":
        return self

    async def __aexit__(self, exc_type, *_) -> None:
        await self._con.aclose()

    #  Sets a key with a value with expire time
    async def set_key(self, key: str, time: int, value: int = 1) -> None:
        await self._con.setex(name=key, time=time, value=value)

    async def get_by_key(self, key: str) -> int | None:
        value = await self._con.get(key)
        return int(value) if value is not None else None

    #  Increments a value stored by the key (mostly used for throttling)
    async def increment_key(self, key: str) -> None:
        await self._con.incr(key)
