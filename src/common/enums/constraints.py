from enum import IntEnum, unique

__all__ = [
    "Constraints"
]


@unique
class Constraints(IntEnum):
    THROTTLING_TIME = 60
    MESSAGES_LIMIT = 5
