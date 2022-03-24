import pyodbc

class Database:
    def __init__(self):
        self.conn = pyodbc.connect(
            r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
            r'DBQ=C:\\Users\\Artem\Desktop\\lab2\\sh_dababase.mdb;'
          
        )
        self.cursor = self.conn.cursor()

    # def insert_dish(self, dish_id, dish_name, description, picture, weight, calories, dish_type, cost):
    #     self.cursor.execute("""INSERT INTO dish VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
    #                         (dish_id, dish_name, description, picture, weight, calories, dish_type, cost))
    #     self.conn.commit()

    def select(self,a):
        self.cursor.execute(a)
        return self.cursor.fetchall()
        #for row in self.cursor.fetchall():
            #print(row)


# db = Database()
# # db.call('id2', 'name1')
# db.select()
