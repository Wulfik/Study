import sqlite3
from DataBase import *


def test():
    connect = sqlite3.connect('DB.db')
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO Goods(name,category_id,price) VALUES(?,(SELECT id FROM Category WHERE name=?),?)",
                   (('test', 'dfbfgfgfhdfh', 35235325)))
    connect.commit()
    connect.close()

test()
print(DataBase.show())
