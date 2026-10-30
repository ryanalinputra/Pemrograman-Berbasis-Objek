from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE kampus")
except Exception as e:
    print(e)
