import math

def hitung_diskon(harga, persen):
        try:
            if harga <= 0:
                raise ValueError("Harga harus lebih dari 0")
            a = harga * persen
            return a
        except ValueError as e:
            print(f"Error: {e}")


class Produk():
    def __init__(self, nama = '', harga = 0):
        self.nama = nama
        self.harga = harga

    def info(self):
        return self.nama

class ProdukElektronik(Produk):
    def __init__(self, nama= '', harga=0, garansi= ''):
        super().__init__(nama, harga)
        self.garansi = garansi
    
    def info(self):
        return f"Nama: {self.nama} \nGaransi: {self.garansi}" 

produk1= ProdukElektronik('Laptop', 5000000, '2 Tahun')

print(produk1.info())
print(f"Diskon: {hitung_diskon(produk1.harga, 0.10)}")
hitung_diskon(0, 0.10)