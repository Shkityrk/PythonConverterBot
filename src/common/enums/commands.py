from enum import StrEnum, unique

__all__ = [
    "TelegramCommand"
]


@unique
class TelegramCommand(StrEnum):
    """Telegram commands for filters to handlers"""
    START_COMMAND = "start"
