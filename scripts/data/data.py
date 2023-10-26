import sqlite3

# создаем бд если еще нет
def create_tables():
    connect = sqlite3.connect('data/db.sql', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id int primary key, first_name varchar(50), last_name varchar(50))')
    connect.commit()
    cursor.close()
    connect.close()

    connect = sqlite3.connect('data/products.sql', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS products (id int primary key, product_name varchar(20), quantity int not null, rating int not null)')
    connect.commit()
    cursor.close()
    connect.close()

# проверка пользователя на регистрацию
def check_registration(id:int):
    connect = sqlite3.connect('data/db.sql', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute("SELECT first_name FROM users WHERE id = ?", (id,))
    result = cursor.fetchone()
    cursor.close()
    connect.close()
    if result is not None:
        return True
    else:
        return False

# добавление нового пользователя в бд
def add_newUser(id:int, first_name:str, last_name:str):
    connect = sqlite3.connect('data/db.sql', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('INSERT INTO users (id, first_name, last_name) VALUES (?, ?, ?)', (id, first_name, last_name))
    connect.commit()
    cursor.close()
    connect.close()