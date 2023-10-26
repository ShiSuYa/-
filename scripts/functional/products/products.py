import sqlite3
from random import randint

# возвращает все товары
def get_all_products():
    conn = sqlite3.connect('data/products.sql', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    temp = ""
    for product in products:
        temp += f"\nID: {product[0]}, Название: {product[1]}, Количество: {product[2]}, Рейтинг: {product[3]}"
    conn.close()

    if (products != []):
        return temp
    return "Товары отсутствуют!"

# добавляет товар
def add_poducts(id:int, product_name:str, quantity:int):
    connect = sqlite3.connect('data/products.sql', check_same_thread=False)
    cursor = connect.cursor()
    cursor.execute('INSERT INTO products (id, product_name, quantity, rating) VALUES (?, ?, ?, ?)', (id, product_name, quantity, randint(0, 5)))
    connect.commit()
    cursor.close()
    connect.close()

# удаляет продукт
def remove_products(product_id:int):
    conn = sqlite3.connect('data/products.sql', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()