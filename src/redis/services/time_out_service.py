from src.redis.redis_repository import RedisRepository

__all__ = [
    "TimeOutService"
]


class TimeOutService:
    _repository: RedisRepository

    def __init__(self) -> None:
        self._repository = RedisRepository()

