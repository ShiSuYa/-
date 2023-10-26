import os
from scripts.bot.bot import bot
from scripts.buttons.buttons import *
from scripts.config.config import main_menu
from scripts.functional.gif.gif import create_gif
from scripts.message.message import get_message_lower
from scripts.functional.health.health import get_health_indicators
from scripts.functional.translation.translation import get_translate_text
from scripts.functional.products.products import get_all_products, add_poducts, remove_products
from scripts.functional.image_editor.image_editor import save_image, get_generated_quality_image, get_generated_bw_image, get_generated_inversion_image

# команда 1
def command1(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
        if (message_lower == "все товары"):
            all_goods = get_all_products()
            markup_reply.add(back_btn)
            bot.send_message(message.chat.id, f'Список всех товаров:\n{all_goods}', reply_markup=markup_reply)
            return
        if (message_lower == "добавить товар"):
            markup_reply.add(back_btn)
            bot.send_message(message.chat.id, 'Введите - id товара, название, количество(через запятую):',
                             reply_markup=markup_reply)
            bot.register_next_step_handler(message, set_products)
            return
        if (message_lower == "убрать товар"):
            markup_reply.add(back_btn)
            bot.send_message(message.chat.id, 'Введите - id товара который нужно убрать:', reply_markup=markup_reply)
            bot.register_next_step_handler(message, remove_product)
            return
    else:
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, "Введите текст!", reply_markup=markup_reply)
        return

# команда 2
def command2(message):
    bot.register_next_step_handler(message, translate)

# команда 3
def command3(message):
    bot.register_next_step_handler(message, health)

# команда 4
def command4(message):
    bot.register_next_step_handler(message, gif_command)

# команда 5
def command5(message):
    bot.register_next_step_handler(message, image_editor)

# запуск фукций перевода
def translate(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
    else:
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, "Введите текст!", reply_markup=markup_reply)
        return

    translate_text = get_translate_text(message.from_user.id, message_lower)

    markup_reply = _create_reply_keyboard_markup()
    markup_reply.add(translate_btn)
    markup_reply.add(back_btn)
    bot.send_message(message.chat.id, f'Перевод текста на русский:\n{translate_text}', reply_markup=markup_reply)

    audio = open(f'scripts/functional/translation/audio_temp/{message.from_user.id}-output.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

# запуск фукций перевода
def gif_command(message):
    markup_reply = _create_reply_keyboard_markup()
    src = f'scripts/functional/gif/images/{message.from_user.id}/'

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            if (os.path.exists(src)):
                clear_gif_path(f'scripts/functional/gif/images/{message.from_user.id}/')

            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
        if (message_lower == "создать"):
            create_gif(message.from_user.id)

            if (os.path.exists(src)):
                clear_gif_path(f'scripts/functional/gif/images/{message.from_user.id}/')

            markup_reply.add(back_btn)
            gif = open(f'scripts/functional/gif/gif_temp/{message.from_user.id}.gif', 'rb')
            bot.send_animation(message.chat.id, gif, reply_markup=markup_reply)
            return

    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if not os.path.exists(src):
            os.makedirs(src)

        src += message.photo[1].file_id + ".jpg"

        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        markup_reply.add(gif1_btn)
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, f'Фото загружено! Создать гиф?', reply_markup=markup_reply)
        bot.register_next_step_handler(message, gif_command)
    except Exception as e:
        print(f"Ошибка: {e}")
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, f'Произошла ошибка!\nПовторите попытку.', reply_markup=markup_reply)
        bot.register_next_step_handler(message, gif_command)

def health(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
        if (message_lower == "рассчитать имт"):
            markup_reply.add(back_btn)
            bot.send_message(message.chat.id, 'Запишите вас вес и рост через запятую.\nПример: 62.8, 183', reply_markup=markup_reply)
            bot.register_next_step_handler(message, health_command1)
            return

def health_command1(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return

        message_lower = message_lower.split(',')

        if (len(message_lower) == 2):
            markup_reply.add(back_btn)
            bmi = get_health_indicators(float(message_lower[0]), float(message_lower[1]))

            bot.send_message(message.chat.id, bmi, reply_markup=markup_reply)
        else:
            markup_reply.add(back_btn)
            bot.send_message(message.chat.id, 'Ошибка ввода!\nПовторите попытку.', reply_markup=markup_reply)
            bot.register_next_step_handler(message, health_command1)

def clear_gif_path(src:str):
    files = os.listdir(src)
    for file_name in files:
        file_path = os.path.join(src, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении {file_path}: {e}')

def image_editor(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return

    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        save_image(message.from_user.id, downloaded_file)

        markup_reply.add(image_editor1_btn, image_editor2_btn, image_editor3_btn)
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, f'Фото загружено! Выберите действие?', reply_markup=markup_reply)
        bot.register_next_step_handler(message, image_action)
    except Exception as e:
        print(f"Ошибка: {e}")
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, f'Произошла ошибка!\nПовторите попытку.', reply_markup=markup_reply)
        bot.register_next_step_handler(message, gif_command)

def image_action(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
        if (message_lower == "улучшить качество"):
            image = get_generated_quality_image(message.from_user.id)

            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            bot.send_message(message.chat.id, 'Улучшение качества фото...', reply_markup=markup_reply)

            bot.send_photo(message.chat.id, image)

            return
        if (message_lower == "черно белое"):
            image = get_generated_bw_image(message.from_user.id)

            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            bot.send_message(message.chat.id, 'Создание черно белого фото...', reply_markup=markup_reply)

            bot.send_photo(message.chat.id, image)

            return
        if (message_lower == "инверсия"):
            image = get_generated_inversion_image(message.from_user.id)

            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            bot.send_message(message.chat.id, 'Создание инверсии фото...', reply_markup=markup_reply)

            bot.send_photo(message.chat.id, image)

            return
        bot.register_next_step_handler(message, image_action)

def set_products(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
    else:
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, "Введите текст!", reply_markup=markup_reply)
        return

    markup_reply.add(back_btn)
    product_info = message_lower.split(', ')

    if (len(product_info) == 3):
        try:
            add_poducts(product_info[0], product_info[1], product_info[2])
            bot.send_message(message.chat.id, 'Товар успешно добавлен!', reply_markup=markup_reply)
            return
        except Exception as e:
            print(f"Ошибка: {e}")
            bot.send_message(message.chat.id, 'Данный товар уже есть на складе!\nИзмените значения.',  reply_markup=markup_reply)
            bot.register_next_step_handler(message, set_products)
    else:
        bot.send_message(message.chat.id, 'Введенные данные не верны!\nПовторите попытку.', reply_markup=markup_reply)
        bot.register_next_step_handler(message, set_products)

def remove_product(message):
    markup_reply = _create_reply_keyboard_markup()

    if (isinstance(message.text, str)):
        message_lower = get_message_lower(message)

        if (message_lower == "назад"):
            markup_reply.add(command1_btn, command2_btn, command3_btn)
            markup_reply.add(command4_btn, command5_btn)
            markup_reply.add(info_btn)
            bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
            return
    else:
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, "Введите текст!", reply_markup=markup_reply)
        return

    markup_reply.add(back_btn)

    try:
        remove_products(message_lower)
        bot.send_message(message.chat.id, 'Товар удален со склада!', reply_markup=markup_reply)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(message.chat.id, 'Введенные данные не верны!\nПовторите попытку.', reply_markup=markup_reply)
        bot.register_next_step_handler(message, set_products)

#возвращает ReplyKeyboardMarkup
def _create_reply_keyboard_markup():
    return types.ReplyKeyboardMarkup(resize_keyboard=True)