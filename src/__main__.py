import asyncio

from src.bot.config import configurate_logger


async def main() -> None:
    configurate_logger()  # Configuration of the logger

if __name__ == '__main__':
    asyncio.run(main())
