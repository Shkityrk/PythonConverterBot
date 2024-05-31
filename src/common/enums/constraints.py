from enum import IntEnum, unique
from src.common.config import DEBUG

__all__ = [
    "Constraints"
]


@unique
class Constraints(IntEnum):
    """Some necessary constraints for services"""
    THROTTLING_TIME = 60
    MESSAGES_LIMIT = 5
    TIME_OUT_TIME = 1 if DEBUG else 60
    #  TODO: SET TIME_OUT_TIME TO 600
