import asyncio

from loguru import logger

from src.app_config import configurate_logger


async def main() -> None:
    configurate_logger()  # Configuration of the logger
    logger.info("LOGGER CONFIGURED")


if __name__ == '__main__':
    asyncio.run(main())
