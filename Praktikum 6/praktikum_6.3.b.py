from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
    val = [
        ('Bella', 'bella', 'bella001', 'Kasir'),
        ('Chacha', 'chacha', 'chacha002', 'Kasir')
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan...") 
except Exception as e:
    print(e)