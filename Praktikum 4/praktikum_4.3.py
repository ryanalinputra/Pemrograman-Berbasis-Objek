class Mahasiswa:
    def __init__(self,val):
        self.nama =val

mhs1 = Mahasiswa('Alya')
mhs2 = Mahasiswa('Agung')
mhs3 = Mahasiswa('Anisa')

print(mhs1.__dict__)
print(mhs2.__dict__)
print(mhs3.__dict__)

class MataKuliah:
    def __init__(self,val):
        self.nama =val

mk1 = MataKuliah('Dasar Pemrograman')
mk2 = MataKuliah('Pemrograman Objek')
mk3 = MataKuliah('Pemrograman Web')

print(mk1.__dict__)
print(mk2.__dict__)
print(mk3.__dict__)

print(mhs1.nama)
print(mhs2.nama)
print(mhs3.nama)

print(mk1.nama)
print(mk2.nama)
print(mk3.nama)

class Mahasiswa:
    def __init__(self, val1, val2):
        self.nama =val1
        self.prodi =val2

mhs1 = Mahasiswa('Alya','Informatika')
mhs2 = Mahasiswa('Agung','Elektro')
mhs3 = Mahasiswa('Anisa','Mesin')

print(mhs1.__dict__)
print(mhs2.__dict__)
print(mhs3.__dict__)

print('Nama mahasiswa 1:',mhs1.nama)
print('Prodi mahasiswa 1:',mhs1.prodi)

print('Nama mahasiswa 2:',mhs2.nama)
print('Prodi mahasiswa 2:',mhs2.prodi)

print('Nama mahasiswa 3:',mhs3.nama)
print('Prodi mahasiswa 3:',mhs3.prodi)

class MataKuliah:
    def __init__(self,val1,val2):
        self.nama =val1
        self.sks =val2

mk1 = MataKuliah('Dasar Pemrograman',2)
mk2 = MataKuliah('Pemrograman Objek',3)
mk3 = MataKuliah('Pemrograman Web',4)

print(mk1.__dict__)
print(mk2.__dict__)
print(mk3.__dict__)

print('Mata Kuliah ',mk1.nama,' memiliki bobot ',mk1.sks,' sks')
print('Mata Kuliah ',mk2.nama,' memiliki bobot ',mk2.sks,' sks')
print('Mata Kuliah ',mk3.nama,' memiliki bobot ',mk3.sks,' sks')

# mhs4=Mahasiswa() # Objek mhs4 tidak bisa terbentuk karena konstruktor memerlukan parameter

class Mahasiswa:
    def __init__(self, val1='', val2=''):
        self.nama =val1
        self.prodi =val2

mhs4=Mahasiswa()
mhs4.nama='Andi'
mhs4.prodi='Akuntansi'
print(mhs4.__dict__)

mhs5=Mahasiswa()
mhs5.nama='Aldo'
print(mhs5.__dict__)

class Mahasiswa:
    nim=0
    def __init__(self, val1='', val2=''):
        self.nama =val1
        self.prodi =val2

mhs6=Mahasiswa()
mhs6.nama='Ajeng'
mhs6.nim=123
mhs6.prodi='Keuangan'
print(mhs6.__dict__)

class MataKuliah:
    prodi = ''
    def __init__(self,val1='',val2=0):
        self.nama =val1
        self.sks =val2

mk4 = MataKuliah()
mk4.nama='Pemrograman Objek'
mk4.sks='2'
mk4.prodi='Informatika'
print(mk4.__dict__)
