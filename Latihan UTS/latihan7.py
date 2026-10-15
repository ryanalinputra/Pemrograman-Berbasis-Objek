class Pegawai():
    def __init__(self, nama = '', gaji = 0):
        self.nama = nama
        self.gaji = gaji
    def hitung_bonus(self):
        a = self.gaji * 0.05
        return a
    def info(self):
        return 'Pegawai biasa'

class Manager(Pegawai):
    def __init__(self, nama = '', gaji = 0, departemen = '' ):
        super().__init__(nama, gaji)
        self.departemen = departemen

    def hitung_bonus(self):
        a = self.gaji * 0.15
        return a

    def info(self):
        return 'Manager'

pegawai1 = Pegawai('Andi', 4000000)
manager1 = Manager('Budi', 8000000, 'IT')

print(pegawai1.nama)
print(pegawai1.gaji)
print(pegawai1.hitung_bonus())
print(pegawai1.info())

print(manager1.nama)
print(manager1.gaji)
print(manager1.departemen)
print(manager1.hitung_bonus())
print(manager1.info())