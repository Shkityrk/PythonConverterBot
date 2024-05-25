from src.bot.root import RootRouter
from src.common.config import THROTTLING, CHECK_TIME_OUT

__all__ = [
    "build_root_router"
]


def build_root_router() -> RootRouter:
    root_router = RootRouter(THROTTLING, CHECK_TIME_OUT)

    return root_router
