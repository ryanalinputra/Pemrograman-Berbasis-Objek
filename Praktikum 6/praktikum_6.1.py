from connectiondb import mydb

print(mydb)

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE my_oop_database")
except Exception as e:
    print(e)