class Hitung:
    hasil=0
    def __init__(self):
        pass
        
    def jumlah(self, a=0, b=0, c=0):
        self.hasil = a+b+c
        return self.hasil

hitung = Hitung()
hasil = hitung.jumlah(a=2,b=3)
print('hasil=', hasil)