from .void import include_void_command_router
from .start import include_start_command_router
from .photo import include_photo_router

__all__ = [
    "include_photo_router",
    "include_start_command_router",
    "include_void_command_router"
]
