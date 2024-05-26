from enum import StrEnum, unique

__all__ = [
    "KeyBases"
]


@unique
class KeyBases(StrEnum):
    """Base for keys in Redis. Key in redis consists of this base + user_id """
    THROTTLING_KEY = "throttling_"
    TIME_OUT_KEY = "time_out_"
