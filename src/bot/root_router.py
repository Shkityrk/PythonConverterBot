from src.bot.root import RootRouter
from src.bot.controllers.commands import (
    include_void_command_router,
    include_start_command_router,
    include_photo_router
)
from src.common.config import THROTTLING

__all__ = [
    "build_root_router"
]


def build_root_router() -> RootRouter:
    root_router = RootRouter(THROTTLING)

    include_start_command_router(root_router)
    include_photo_router(root_router)
    include_void_command_router(root_router)

    return root_router
