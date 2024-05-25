import asyncio

from loguru import logger

from src.common.config import configurate_logger
from src.bot import bot, dispatcher


async def main() -> None:
    configurate_logger()  # Configuration of the logger
    logger.info("LOGGER CONFIGURED")

    logger.info("STARTING THE BOT...")
    await bot.delete_webhook(drop_pending_updates=True)  # Need to drop all updates before bot was turned on
    await dispatcher.start_polling(bot)  # Starting polling. I guess I'll switch to webhook later


if __name__ == '__main__':
    asyncio.run(main())
