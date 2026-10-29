from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE user (nama VARCHAR(55), username VARCHAR(55) PRIMARY KEY, password VARCHAR(55))")
    mycursor.execute("ALTER TABLE user ADD COLUMN level VARCHAR(10)")
except Exception as e:
    print(e)