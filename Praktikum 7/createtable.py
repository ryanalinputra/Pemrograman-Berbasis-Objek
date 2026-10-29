from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE barang (id VARCHAR(10) PRIMARY KEY, nama VARCHAR(55), stok INT(11), harga INT(11), kategori VARCHAR(50))")
except Exception as e:
    print(e)
