from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO mahasiswa (nim, nama, jurusan, umur) VALUES (%s, %s, %s, %s)"
    val = [
        ('253101001', 'Aldo', 'Teknik Informatika', 20),
        ('253101002', 'Intar', 'Sistem Informasi', 21),
        ('253101003', 'Ryan', 'Manajemen Informatika', 19)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan...")

    sql = "UPDATE mahasiswa SET nama = %s WHERE nim = %s"
    val = ('Aldo Wijaya', '253101001')
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil diupdate.")

    sql = "DELETE FROM mahasiswa WHERE nim = %s"
    val = ('253101003', )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil dihapus.")

    mycursor.execute("SELECT * FROM mahasiswa")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

except Exception as e:
    print(e)