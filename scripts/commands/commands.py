from scripts.config.config import info
from scripts.functional.functional import *
from scripts.data.data import check_registration, add_newUser

# ответ на команду /start от пользователя
@bot.message_handler(commands=['start'])
def _start(message):
    # если пользователь уже есть в бд то ничего не делаем
    if (check_registration(message.from_user.id) is not False):
        return

    # проверка на наличии фамилии у пользователя
    try:
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reply.add(menu_btn)

        if (message.from_user.last_name is not None):
            # если есть то добавляем в бд с фамилией
            add_newUser(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
            bot.send_message(message.chat.id, f'{message.from_user.first_name} {message.from_user.last_name}, вы успешно зарегестрированы!', reply_markup=markup_reply)
        else:
            # если нет то добавляем в бд без фамилии
            add_newUser(message.from_user.id, message.from_user.first_name, "")
            bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы успешно зарегестрированы!', reply_markup=markup_reply)
    except Exception as e:
        # в случае ошибки выводим ее в консоль
        return print(f"Ошибка: {e}")

# ответ бота на обычные сообщения
@bot.message_handler()
def _standartMessage(message):
    # получение текста в нижнем регистре
    message_lower = get_message_lower(message)
    # создание кнопок под клавиатурой
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # ответы на сообщения пользователя
    if (message_lower == 'меню' or message_lower == 'назад'):
        markup_reply.add(command1_btn, command2_btn, command3_btn)
        markup_reply.add(command4_btn, command5_btn)
        markup_reply.add(info_btn)
        bot.send_message(message.chat.id, main_menu, reply_markup=markup_reply)
        return
    if (message_lower == "товары"):
        markup_reply.add(product1_btn, product2_btn, product3_btn)
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, '=== Товары ===\n\n1) Все товары\n2)Добавить товар\n3) Убрать товар', reply_markup=markup_reply)
        bot.register_next_step_handler(message, command1)
        return
    if (message_lower == "переводчик" or message_lower == "продолжить перевод"):
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, '=== Переводчик ===\n\nВведите текст на любом языке:', reply_markup=markup_reply)
        command2(message)
        return
    if (message_lower == "здоровье"):
        markup_reply.add(health1_btn)
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, '=== Здоровье ===\n\nРассчитать ИМТ', reply_markup=markup_reply)
        command3(message)
        return
    if (message_lower == "гиф"):
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, '=== Гиф ===\n\nДобавьте фото(по одному):', reply_markup=markup_reply)
        command4(message)
        return
    if (message_lower == "редактор изображения"):
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, '=== Редактор Изображения ===\n\nДобавьте фото(одно):', reply_markup=markup_reply)
        command5(message)
        return
    if (message_lower == "информация"):
        markup_reply.add(back_btn)
        bot.send_message(message.chat.id, info, reply_markup=markup_reply)
        return