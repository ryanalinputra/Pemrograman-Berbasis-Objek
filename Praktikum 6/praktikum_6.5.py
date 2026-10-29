from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "UPDATE user SET level = %s WHERE username = %s"
    val = ('Kasir', 'aldo')
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil diupdate.")
    
except Exception as e:
    print(e)