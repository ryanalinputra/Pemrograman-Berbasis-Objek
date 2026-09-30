class Mahasiswa:
    nim=0
    def __init__(self):
        self.nama =''
        self.prodi =''

    def set_atribut(self,val1='', val2=''):
        self.nama =val1
        self.prodi =val2

    def get_atribut(self):
        print("Nama \t:",self.nama,
              "\nNIM \t:",self.nim,
              "\nProdi\t:",self.prodi)

mhs1 = Mahasiswa()
mhs1.set_atribut('Alya','informatika')
mhs1.nim=111
print(mhs1.get_atribut())

mhs2 = Mahasiswa()
mhs2.set_atribut('Agung','Elektro')
print(mhs2.get_atribut())

mhs3 = Mahasiswa()
print(mhs3.get_atribut())

mhs4 = Mahasiswa()
mhs4.nama='Anisa'
mhs4.alamat='Kediri'
mhs4.nim=133
print(mhs4.__dict__)
print(mhs4.get_atribut())

class MataKuliah:
    prodi = ''
    def __init__(self):
        self.nama =''
        self.sks =0

    def set_atribut(self,val1='', val2=0):
        self.nama =val1
        self.sks =val2

    def get_atribut(self):
        print("Nama \t:",self.nama,
              "\nsks \t:",self.sks)

mk1 = MataKuliah()
mk1.set_atribut('Dasar Pemrograman','2')
print(mk1.get_atribut())

mk2 = MataKuliah()
mk2.set_atribut('Pemrograman Objek')
print(mk2.get_atribut())

mk3 = MataKuliah()
print(mk3.get_atribut())

mk4 = MataKuliah()
mk4.nama='Basis Data'
mk4.sks=3
print(mk4.__dict__)
print(mk4.get_atribut())
