import asyncio

from src.app_config import configurate_logger


async def main() -> None:
    configurate_logger()  # Configuration of the logger

if __name__ == '__main__':
    asyncio.run(main())
