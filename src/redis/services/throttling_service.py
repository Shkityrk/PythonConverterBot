from src.redis.redis_repository import RedisRepository
from src.common.enums import KeyBases, Constraints

__all__ = [
    "ThrottlingService"
]


class ThrottlingService:
    _repository: RedisRepository

    def __init__(self):
        self._repository = RedisRepository()

    async def need_to_throttle(self, user_id: str) -> bool:
        async with self._repository as repository:
            messages_count = await repository.get_by_key(KeyBases.THROTTLING_KEY + user_id)
            if messages_count is None:
                await repository.set_key(KeyBases.THROTTLING_KEY + user_id, int(Constraints.THROTTLING_TIME))
                return False

            # NEED TO PARSE CONSTRAINT TO INT IDK WHY ENUMS WORKS SO BADLY
            if messages_count > int(Constraints.MESSAGES_LIMIT): return True
            await repository.increment_key(KeyBases.THROTTLING_KEY + user_id)
            return False
