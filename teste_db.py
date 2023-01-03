import sqlite3

connection = sqlite3.connect('ecommerce2.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS dados2 (cart integer primary key autoincrement)')

create_table()

cursor.execute("INSERT INTO dados2 (cart) VALUES('1')")
connection.commit()
connection.close()
