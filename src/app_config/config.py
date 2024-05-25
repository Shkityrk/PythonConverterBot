from pathlib import Path

from src.app_config.env import StrEnv

__all__ = [
    "BOT_TOKEN",
    "LOGGING_PATH"
]


BOT_TOKEN: str = StrEnv("BOT_TOKEN")
LOGGING_PATH: Path = Path(StrEnv("LOGGING_PATH"))
