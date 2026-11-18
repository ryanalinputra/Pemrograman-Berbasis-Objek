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
                self.insert_data_log(User.current_user, "Login")
                return str(level[0])
            return None
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

    def select_data_tabel(self):
        try:
            sql = "SELECT nama, username, password, level FROM user"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def insert_data(self, val1, val2, val3, val4):
        try:
            sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            self.insert_data_log(User.current_user, f"Tambah user {val2}")
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update_data(self, val1, val2, val3, val4):
        try:
            sql = "UPDATE user SET nama= %s, password= %s, level = %s WHERE username = %s"
            val = (val1, val2, val3, val4)
            mycursor.execute(sql, val)
            mydb.commit()
            self.insert_data_log(User.current_user, f"Ubah user {val4}")
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete_data(self, val1):
        try:
            sql = "DELETE FROM user WHERE username = %s"
            value = (val1,)
            mycursor.execute(sql, value)
            mydb.commit()
            self.insert_data_log(User.current_user, f"Hapus user {val1}")
            print(mycursor.rowcount, "Data berhasil dihapus")
        except Exception as e:
            print(e)
    
    def select_data_tabel_log(self):
        try:
            sql = "SELECT tanggal_jam, user, keterangan FROM log"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def insert_data_log(self, val1, val2):
        try:
            sql = "INSERT INTO log (tanggal_jam, user, keterangan) VALUES (NOW(), %s, %s)"
            val = (val1, val2)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(e)
