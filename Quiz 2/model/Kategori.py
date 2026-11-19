from model.connectiondb import mydb

mycursor = mydb.cursor()

class Kategori:
    def __init__(self):
        self

    def get_Data(self):
        try:
            sql = "SELECT id, kategori FROM kategori"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def insert(self, val1, val2):
        try:
            sql = "INSERT INTO kategori (id, kategori) VALUES (%s, %s)"
            val = (val1, val2)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update(self, val1, val2):
        try:
            sql = "UPDATE kategori SET kategori= %s WHERE id = %s"
            val = (val1, val2)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete(self, val1):
        try:
            sql = "DELETE FROM kategori WHERE id = %s"
            value = (val1,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
        except Exception as e:
            print(e)
