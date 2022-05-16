import sqlite3
import json
class DataBase():
    def create_table():
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS 'Category'(
                            id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE
                )
                """)
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS 'Goods'(
                                   id INTEGER PRIMARY KEY,
                                   name TEXT,
                                   category_id INTEGER NOT NULL,
                                   price INTEGER NOT NULL,
                                   FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE
                       )
                       """)
        connect.commit()
        connect.close()

    def add_category(new_category):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Category(name) VALUES (?)",((str(new_category),)))
        connect.commit()
        connect.close()

    def delete_category(category_name):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM Goods WHERE category_id=(SELECT id FROM Category WHERE name=(?))", ((str(category_name),)))
        cursor.execute(f"DELETE FROM Category WHERE name=?", ((str(category_name),)))
        connect.commit()
        connect.close()

    def check_unique_category(category_name):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT id FROM 'Category' WHERE name=?", ((str(category_name),)))
        category_list = cursor.fetchall()
        connect.commit()
        connect.close()
        print(category_list)
        if not category_list:
            return False
        else:
            return True

    def check_unique_goods(category_name, goods_name):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT name FROM 'Goods' WHERE category_id=(SELECT id FROM Category WHERE name=(?))", ((str(category_name),)))
        category_list = cursor.fetchall()
        connect.commit()
        connect.close()
        is_uniq = False
        for item in category_list:
            if goods_name in item[0]:
                is_uniq=True

        return is_uniq



    def get_category():
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT name FROM 'Category'")
        category = cursor.fetchall()
        category_list = []
        for name in category:
            category_list.append(name[0])
        connect.commit()
        connect.close()
        return category_list

    def get_goods(category_name):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM Goods WHERE Goods.category_id = (SELECT id FROM Category WHERE name=(?))",((category_name),))
        goods = cursor.fetchall()
        connect.commit()
        connect.close()
        return goods

    def add_goods(name,category,price):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Goods(name,category_id,price) VALUES(?,(SELECT id FROM Category WHERE name=?),?)",((name,category,price)))
        connect.commit()
        connect.close()

    def delete_goods(name,category):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"DELETE FROM Goods WHERE name=? AND category_id=(SELECT id FROM Category WHERE name=?)", ((str(name),str(category))))
        connect.commit()
        connect.close()

    def update_name(new_name, id):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"UPDATE Goods SET name = ? WHERE id = ?",(str(new_name),(id),))
        connect.commit()
        connect.close()

    def update_price(price,id):
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"UPDATE Goods SET price = ? WHERE id=?",((int(price), id)))
        connect.commit()
        connect.close()

    def show():
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM 'Category'")
        data = cursor.fetchall()
        cursor.execute(f"SELECT * FROM 'Goods'")
        data1 = cursor.fetchall()
        connect.commit()
        connect.close()
        return data, data1

    def test():
        connect = sqlite3.connect('DB.db')
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO Goods(name,category_id,price) VALUES(?,(SELECT id FROM Category WHERE name=?),?)",
                       (('test', 'dfbfgfgfhdfh', price)))
        connect.commit()
        connect.close()
# DataBase.create_table()
# DataBase.add_category(1)
# print(DataBase.show())