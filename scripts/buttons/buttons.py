from telebot import types

# кнопки под клавиатурой

back_btn = types.KeyboardButton('Назад')
menu_btn = types.KeyboardButton('Меню')
info_btn = types.KeyboardButton('Информация')

command1_btn = types.KeyboardButton('Товары')
command2_btn = types.KeyboardButton('Переводчик')
command3_btn = types.KeyboardButton('Здоровье')
command4_btn = types.KeyboardButton('Гиф')
command5_btn = types.KeyboardButton('Редактор изображения')

product1_btn = types.KeyboardButton('Все товары')
product2_btn = types.KeyboardButton('Добавить товар')
product3_btn = types.KeyboardButton('Убрать товар')

image_editor1_btn = types.KeyboardButton('Улучшить качество')
image_editor2_btn = types.KeyboardButton('Черно белое')
image_editor3_btn = types.KeyboardButton('Инверсия')

health1_btn = types.KeyboardButton('Рассчитать ИМТ')

gif1_btn = types.KeyboardButton('Создать')

translate_btn = types.KeyboardButton('Продолжить перевод')