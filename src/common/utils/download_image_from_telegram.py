from PIL import Image

from src.bot.init_bot import bot

__all__ = [
    "download_image_from_telegram"
]


async def download_image_from_telegram(file_id: str) -> Image:
    photo_path = (await bot.get_file(file_id)).file_path
    await bot.download_file(photo_path, "media/photo.png")

    return Image.open("media/photo.png")
