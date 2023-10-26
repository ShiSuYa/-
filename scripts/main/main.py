from scripts.commands.commands import *
from scripts.data.data import create_tables

# старт бота, запуск основных функций бота
def Start():

    try:
        # создание бд если она еще не создана
        create_tables()

        # успешный старт бота
        print("Bot Started!")

        # старт пула бота, и включение функции постоянного актива
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        # в случае ошибки выводим ее в консоль
        return print(f"Ошибка: {e}")

# точка входа
if __name__ == '__main__':
    Start()