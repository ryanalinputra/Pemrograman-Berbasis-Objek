class Kendaraan():
    def __init__(self, merk= '', warna= ''):
        self.merk = merk
        self.warna = warna

class Mobil(Kendaraan):
    def __init__(self, merk= '', warna= '', jumlah_pintu= 0 ):
        super().__init__(merk, warna, jumlah_pintu)
        self.jumlah_pintu = jumlah_pintu

mobil1 = Mobil(
    'Toyota',
    'Hitam',
    4
)
        