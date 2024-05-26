from aiogram import Router


from src.bot.root import RootRouter

__all__ = [
    "include_void_command_router",
]

void_message_router = Router()


def include_void_command_router(root_router: RootRouter) -> None:
    root_router.include_router(void_message_router)


@void_message_router.message(flags={"void_command": True})
async def void_command() -> None:
    pass
