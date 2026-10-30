from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE mahasiswa (nim VARCHAR(55) PRIMARY KEY, nama VARCHAR(55))")
except Exception as e:
    print(e)