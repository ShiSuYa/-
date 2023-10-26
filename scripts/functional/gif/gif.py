import os
from PIL import Image

def create_gif(id:int, duration=500):
    images_folder = f'scripts/functional/gif/images/{id}/'

    # массив кадров
    frames = []
    # получение изображений из папки с расширениями '.png', '.jpg', '.jpeg'
    image_files = [f for f in os.listdir(images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # получаем каждое изображение из image_files и добавляем его в frames
    for image_file in image_files:
        frame = Image.open(f'{images_folder}/{image_file}')
        frames.append(frame)

    # сохраняем GIF
    frames[0].save(
        f'scripts/functional/gif/gif_temp/{id}.gif',
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )