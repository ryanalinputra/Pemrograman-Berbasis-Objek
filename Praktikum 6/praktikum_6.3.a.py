from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (nama, username, password, level) VALUES (%s, %s, %s, %s)"
    val = ("Aldo", "aldo", "aldo000", "Admin")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil ditambahkan...") 
except Exception as e:
    print(e)