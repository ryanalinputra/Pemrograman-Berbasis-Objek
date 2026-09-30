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

mhs4 = Mahasiswa()
mhs4.nama='Anisa'
mhs4.alamat='Kediri'
mhs4.nim=133

print(hasattr(mhs1, 'nim'))
print(hasattr(mhs1, 'nama'))
print(hasattr(mhs1, 'prodi'))
print(hasattr(mhs1, 'alamat'))

print(hasattr(mhs4, 'nim'))
print(hasattr(mhs4, 'nama'))
print(hasattr(mhs4, 'prodi'))
print(hasattr(mhs4, 'alamat'))

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

mk4 = MataKuliah()
mk4.nama='Basis Data'
mk4.sks=3

print(hasattr(mk1, 'nama'))
print(hasattr(mk1, 'sks'))

print(hasattr(mk4, 'nama'))
print(hasattr(mk4, 'sks'))
