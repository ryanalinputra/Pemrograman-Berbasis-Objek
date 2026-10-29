from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "DELETE from user WHERE username = %s"
    val = ('aldo', )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil dihapus.")
    
except Exception as e:
    print(e)