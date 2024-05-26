from enum import StrEnum, unique

__all__ = [
    "TelegramCommand"
]


@unique
class TelegramCommand(StrEnum):
    START_COMMAND = "start"
