from connectiondb import mydb

mycursor = mydb.cursor()

class User:
    def __init__(self):
        self

    def login(self, val1, val2):
        try:
            sql = "SELECT level FROM user WHERE username = %s AND password = %s"
            val = (val1, val2)
            mycursor.execute(sql, val)
            level = mycursor.fetchone()
            return str(level[0])
        except Exception as e:
            print(e)

    def select_data(self):
        try:
            sql = "SELECT * FROM user"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        except Exception as e:
            print(e)

    def insert_data(self, val1, val2, val3, val4):
        try:
            sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update_data(self, val1, val2, val3, val4):
        try:
            sql = "UPDATE user SET nama= %s, password= %s, level = %s WHERE username = %s"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete_data(self, val1):
        try:
            sql = "DELETE FROM user WHERE username = %s"
            value = (val1,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
        except Exception as e:
            print(e)

    def insert_data_log(self, val1, val2):
        try:
            sql = "INSERT INTO log (tanggal_jam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (val1, val2)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)
