class Kendaraan():
    jumlah_kendaraan = 0
    def __init__(self, merk = ''):
        self.merk = merk
        Kendaraan.jumlah_kendaraan += 1
       

class Mobil(Kendaraan):
    def __init__(self, merk = '', warna= ''):
        super().__init__(merk)
        self.warna = warna
        

mobil1= Mobil('Toyota', 'Hitam')
mobil2= Mobil('Honda', 'Putih')

print(mobil1.merk)    
print(mobil1.warna)     
print(mobil2.merk)    
print(mobil2.warna)    
print(Kendaraan.jumlah_kendaraan)    