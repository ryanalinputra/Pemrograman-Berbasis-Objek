class Hewan():
    def __init__(self, nama = ''):
        self.nama = nama
    def bersuara(self):
        return 'Suara Hewan'

class Kucing(Hewan):
    def __init__(self,nama = '', warna = ''):
        super().__init__(nama)
        self.warna = warna
    def bersuara(self):
        return 'Meong'

kucing1 = Kucing(
    'Milo',
    'Putih'
)
print(kucing1.nama)
print(kucing1.warna)
print(kucing1.bersuara())