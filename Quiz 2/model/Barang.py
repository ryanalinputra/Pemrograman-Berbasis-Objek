from model.connectiondb import mydb
from model.Kategori import Kategori

mycursor = mydb.cursor()

class Barang:
    def __init__(self):
        self
        self.kategori = Kategori()

    def select_all(self):
        try:
            sql = "SELECT barang.kode, barang.nama, barang.stok, barang.harga, kategori.kategori FROM barang JOIN kategori ON barang.id_kategori = kategori.id"
            mycursor.execute(sql)
            return mycursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def select_by_id(self, val1):
        try:
            sql = "SELECT barang.kode, barang.nama, barang.stok, barang.harga, kategori.kategori FROM barang JOIN kategori ON barang.id_kategori = kategori.id WHERE barang.kode = %s"
            val = (val1,)
            mycursor.execute(sql, val)
            return mycursor.fetchone()
        except Exception as e:
            print(e)
            return None

    def insert(self, val1, val2, val3, val4, val5):
        try:
            sql = "INSERT INTO barang (kode, nama, stok, harga, id_kategori) VALUES (%s, %s, %s, %s, %s)"
            val = (val1, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil ditambahkan...")
        except Exception as e:
            print(e)

    def update(self, val1, val2, val3, val4, val5):
        try:
            sql = "UPDATE barang SET nama= %s, stok= %s, harga = %s, id_kategori = %s WHERE kode = %s"
            val = (val1, val2, val3, val4, val5)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil diupdate.")
        except Exception as e:
            print(e)

    def delete(self, val1):
        try:
            sql = "DELETE FROM barang WHERE kode = %s"
            value = (val1,)
            mycursor.execute(sql, value)
            mydb.commit()
            print(mycursor.rowcount, "Data berhasil dihapus")
        except Exception as e:
            print(e)
