from src.redis.redis_repository import RedisRepository
from src.common.enums import KeyBases, Constraints

__all__ = [
    "TimeOutService"
]


class TimeOutService:
    _repository: RedisRepository

    def __init__(self) -> None:
        self._repository = RedisRepository()

    async def is_timed_out(self, user_id: str) -> bool:
        async with self._repository as repository:
            has_converted_photo = await repository.get_by_key(KeyBases.TIME_OUT_KEY + user_id)
            if has_converted_photo is None:
                await repository.set_key(KeyBases.TIME_OUT_KEY + user_id, int(Constraints.TIME_OUT_TIME))
                return False

            return True
