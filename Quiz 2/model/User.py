from model.connectiondb import mydb

mycursor = mydb.cursor()

class User:
    current_user = "Unknown"

    def __init__(self):
        self

    def login(self, val1, val2):
        try:
            sql = "SELECT level FROM user WHERE username = %s AND password = %s"
            val = (val1, val2)
            mycursor.execute(sql, val)
            level = mycursor.fetchone()
            if level:
                User.current_user = val1
                return str(level[0])
            return None
        except Exception as e:
            print(e)

    def select_all(self):
        try:
            sql = "SELECT nama, username, password, level FROM user"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def select_by_id(self, val1):
        try:
            sql = "SELECT nama, username, password, level FROM user WHERE username = %s"
            val = (val1,)
            mycursor.execute(sql, val)
            return mycursor.fetchone()
        except Exception as e:
            print(e)
            return None

    def insert(self, val1, val2, val3, val4):
        try:
            sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update(self, val1, val2, val3, val4):
        try:
            sql = "UPDATE user SET nama= %s, password= %s, level = %s WHERE username = %s"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete(self, val1):
        try:
            sql = "DELETE FROM user WHERE username = %s"
            value = (val1,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
        except Exception as e:
            print(e)
