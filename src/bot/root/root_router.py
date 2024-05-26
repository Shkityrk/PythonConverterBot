from aiogram import Router, Dispatcher

from src.common.exceptions import RootRouterParentError
from src.bot.root.middlewares import (
    CatchExceptionMiddleware,
    SetThrottlingMiddleware
)

__all__ = [
    "RootRouter"
]


class RootRouter(Router):
    def __init__(self, throttling: bool, name: str | None = None) -> None:
        super().__init__(name=name)

        if self.parent_router is not None and not isinstance(
                self.parent_router,
                Dispatcher
        ):
            raise RootRouterParentError("Only Dispatcher can be parent for RootRouter.")

        self._add_catch_exception_middleware()
        if throttling: self._add_set_throttling_middleware()

    def _add_catch_exception_middleware(self) -> None:
        self.message.middleware(CatchExceptionMiddleware())
        self.callback_query.middleware(CatchExceptionMiddleware())

    def _add_set_throttling_middleware(self) -> None:
        self.message.middleware(SetThrottlingMiddleware())
        self.callback_query.middleware(SetThrottlingMiddleware())
