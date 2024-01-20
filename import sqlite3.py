import sqlite3
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()


#Таблица Пользователи
T_User='''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    number INTEGER NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
)
'''
cursor.execute(T_User)
conn.commit()


#Таблица Блюда
T_Dishes ='''
CREATE TABLE IF NOT EXISTS Dishes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    weight INTEGER NOT NULL,
    composition TEXT NOT NULL
)
'''
cursor.execute(T_Dishes)
conn.commit()

# Таблица Аккаунты рабочих
T_Employee_accounts='''
CREATE TABLE IF NOT EXISTS Employee_accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    work_schedule DATE NOT NULL,
    password TEXT NOT NULL
)
'''
cursor.execute(T_Employee_accounts)
conn.commit()

#Таблича Заказы
T_Orders='''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    address_user TEXT NOT NULL,
    dishes TEXT NOT NULL,
    quantity TEXT NOT NULL,
    FOREIGN KEY (user) REFERENCES User (name) ON DELETE CASCADE,
    FOREIGN KEY (address_user) REFERENCES User (address) ON DELETE CASCADE,
    FOREIGN KEY (dishes) REFERENCES Dishes (name) ON DELETE CASCADE

)
'''
cursor.execute(T_Orders)
conn.commit()
