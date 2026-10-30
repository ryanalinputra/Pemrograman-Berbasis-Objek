from connectiondb import mydb

mycursor = mydb.cursor()

class Barang:
    def __init__(self):
        self

    def select_data(self):
        try:
            sql = "SELECT * FROM barang"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        except Exception as e:
            print(e)

    def insert_data(self, val1, val2, val3, val4, val5):
        try:
            sql = "INSERT INTO barang (id, nama, stok, harga, kategori) VALUES (%s, %s, %s, %s, %s)"
            val = (val1, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update_data(self, val1, val2, val3, val4, val5):
        try:
            sql = "UPDATE barang SET nama= %s, stok= %s, harga = %s, kategori = %s WHERE id = %s"
            val = (val1, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete_data(self, val1):
        try:
            sql = "DELETE FROM barang WHERE id = %s"
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
