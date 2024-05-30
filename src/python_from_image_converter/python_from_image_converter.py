import os

import pytesseract
from PIL import Image
from loguru import logger

from src.common.config import TESSERACT_PATH


__all__ = [
    "PythonFromImageConverter"
]

pytesseract.pytesseract.tesseract_cmd = os.path.join(TESSERACT_PATH, 'tesseract')


class PythonFromImageConverter:
    image: Image

    def __init__(self, image: Image) -> None:
        self.image = image

    def convert_image_to_python(self) -> str:
        # Распознание текста с учетом пробелов, табуляций и переносов строк
        text = pytesseract.image_to_string(self.image, output_type=pytesseract.Output.BYTES, config='--psm 3')
        # Декодирование текста из байтов в строку
        decoded_text = text.decode('utf-8')

        # Фильтрация текста
        lines = []
        for line in decoded_text.split('\n'):
            # Игнорирование строк, начинающихся с символа #
            if not line.strip().startswith('#'):
                # Исключение строк, содержащих ключевые слова на последнем месте
                if not (line.strip().endswith('usage') or line.strip().endswith('usages')):
                    # Добавление строки в список строк
                    lines.append(line)

        # Сборка отфильтрованного текста
        return '\n'.join(lines)
