from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE username = %s"
    val = ("aldo", )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    print(e)