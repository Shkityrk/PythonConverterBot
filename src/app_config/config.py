from pathlib import Path

from src.app_config.env import StrEnv, IntEnv

__all__ = [
    "BOT_TOKEN",
    "LOGGING_PATH",
    "REDIS_HOST",
    "REDIS_PORT",
]


BOT_TOKEN: str = StrEnv("BOT_TOKEN")
LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))

REDIS_HOST: str = StrEnv("REDIS_HOST")
REDIS_PORT: int = IntEnv("REDIS_PORT")

