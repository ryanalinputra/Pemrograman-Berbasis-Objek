from connectiondb import mydb

try:
    mycursor = mydb.cursor()
    mycursor.execute("ALTER TABLE mahasiswa ADD COLUMN jurusan VARCHAR(55)")
    mycursor.execute("ALTER TABLE mahasiswa ADD COLUMN umur INT")
except Exception as e:
    print(e)