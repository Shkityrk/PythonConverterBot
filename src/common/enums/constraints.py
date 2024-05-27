from enum import IntEnum, unique

__all__ = [
    "Constraints"
]


@unique
class Constraints(IntEnum):
    """Some necessary constraints for services"""
    THROTTLING_TIME = 60
    MESSAGES_LIMIT = 5
    TIME_OUT_TIME = 600
