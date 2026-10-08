class Kucing():
    warna = 'Kuning'
    def bersuara(self):
        return 'meow'

class Sapi():
    warna = 'Putih'
    def bersuara(self):
        return 'Moo'

Kiwi = Kucing()
print(Kiwi.warna)
print(Kiwi.bersuara())

api = Sapi()
print(api.warna)
print(api.bersuara())

class Mamalia():
    ekor = 'Ada / Tidak ada'
    def bergerak(self):
        return 'Berjalan/ Berenang'

class Kucing(Mamalia):
    ekor ='Ada'
    def bergerak(Self):
        return 'Berjalan'

class British (Kucing):
    pass

Kiwi = British()
print(Kiwi.ekor)
print(Kiwi.bergerak())

class British:
    warna = 'Kuning'
    berat = True
    def sifat(self):
        return 'Lincah'

class Ragdoll:
    warna = 'Putih'
    tinggi = True
    def sifat(self):
        return 'Tenang'

class Campuran (British, Ragdoll):
    pass

Kiwi = Campuran()
print(Kiwi.warna)
print(Kiwi.berat)
print(Kiwi.tinggi)
print(Kiwi.sifat())

class British:
    warna = 'Kuning'
    berat = True
    def sifat(self):
        return 'Lincah'

class Ragdoll:
    warna = 'Putih'
    tinggi = True
    def sifat(self):
        return 'Tenang'

class Campuran (Ragdoll, British):
    pass

Kiwi = Campuran()
print(Kiwi.warna)
print(Kiwi.berat)
print(Kiwi.tinggi)
print(Kiwi.sifat())
