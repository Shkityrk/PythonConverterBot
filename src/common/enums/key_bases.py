from enum import StrEnum, unique

__all__ = [
    "KeyBases"
]


@unique
class KeyBases(StrEnum):
    THROTTLING_KEY = "throttling_"
    TIME_OUT_KEY = "time_out_"
