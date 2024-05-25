from src.redis.redis_repository import RedisRepository

__all__ = [
    "ThrottlingService"
]


class ThrottlingService:
    _repository: RedisRepository

    def __init__(self) -> None:
        self._repository = RedisRepository()

