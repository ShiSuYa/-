import os
from PIL import Image, ImageFilter, ImageOps

# возвращает измененное изображение
def get_generated_quality_image(id:int):
    # получение изображения
    image = _get_image_in_folder(id)

    # увеличение резкости
    image = image.filter(ImageFilter.SHARPEN)

    return image

# возвращает измененное изображение
def get_generated_bw_image(id:int):
    # получение изображения
    image = _get_image_in_folder(id)

    # преобразовываем в черно белое
    image = image.convert('L')

    return image

# возвращает измененное изображение
def get_generated_inversion_image(id:int):
    # получение изображения
    image = _get_image_in_folder(id)

    # создаем инверсию изображения
    image = ImageOps.invert(image)

    return image

# сохраняет изображение
def save_image(id:int, file):
    # получение пути
    src = f'scripts/functional/image_editor/images/'

    # создаем папку если еще нет
    if not os.path.exists(src):
        os.makedirs(src)

    # добавляем название файла и расширение
    src += f"{id}.jpg"

    # создаем файл
    with open(src, 'wb') as new_file:
        new_file.write(file)

# возаращает изображение из папки
def _get_image_in_folder(id:int):
    image = Image.open(f'scripts/functional/image_editor/images/{id}.jpg')
    return image