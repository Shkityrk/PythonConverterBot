from pathlib import Path

from src.common.config.env import StrEnv, IntEnv, BoolEnv

__all__ = [
    "DEBUG",
    "BOT_TOKEN",
    "LOGGING_PATH",
    "THROTTLING",
    "CHECK_TIME_OUT",
    "REDIS_HOST",
    "REDIS_PORT",
    "TESSERACT_PATH"
]


DEBUG: bool = BoolEnv("DEBUG")

BOT_TOKEN: str = StrEnv("BOT_TOKEN")
LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))

THROTTLING: bool = BoolEnv("THROTTLING")
CHECK_TIME_OUT: bool = BoolEnv("CHECK_TIME_OUT")

REDIS_HOST: str = StrEnv("REDIS_HOST")
REDIS_PORT: int = IntEnv("REDIS_PORT")

TESSERACT_PATH: str = StrEnv("TESSERACT_PATH")

