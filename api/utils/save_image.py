import datetime
import os

from PIL import Image, ImageFile


def image_add_origin(image, folder):
    # Создаем папку по текущей дате, если она еще не существует
    current_date = datetime.datetime.now().date()
    folder_path = os.path.join(folder, str(current_date))
    os.makedirs(folder_path, exist_ok=True)

    # Генерируем имя файла изображения на основе текущего времени
    current_time = datetime.datetime.now().strftime("%H%M%S%f")
    file_extension = os.path.splitext(image.filename)[1]
    image_path = os.path.join(folder_path, f"{current_time}{file_extension}")

    # Сохраняем изображение
    image_object = Image.open(image.file)
    image_object.save(image_path, format='webp', quality=100, optimize=True)

    return image_path
