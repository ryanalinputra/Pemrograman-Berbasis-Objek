class Kendaraan():
    jumlah_kendaraan = 0
    def __init__(self, merk = '', warna = ''):
        self.merk = merk
        self.warna = warna
        Kendaraan.jumlah_kendaraan += 1
    def info(self):
        return 'Kendaraan Umum' 
       

class Mobil(Kendaraan):
    def __init__(self, merk = '', warna= '', jumlah_pintu = 0):
        super().__init__(merk, warna)
        self.jumlah_pintu = jumlah_pintu
    def info(self):
        return 'Mobil pribadi' 
         
mobil1= Mobil('Toyota', 'Hitam', 4)
mobil2= Mobil('Honda', 'Putih', 2)

print(mobil1.merk)    
print(mobil1.warna)
print(mobil1.jumlah_pintu)
print(mobil1.info())

print(mobil2.merk)    
print(mobil2.warna) 
print(mobil2.jumlah_pintu)
print(mobil2.info())
print(Kendaraan.jumlah_kendaraan)         