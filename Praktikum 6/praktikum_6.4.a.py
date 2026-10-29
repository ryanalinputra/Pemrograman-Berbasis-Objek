from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM user")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    print(e)