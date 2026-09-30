class Mahasiswa:
    nim=0
    def __init__(self):
        self.nama =''
        self.__prodi =''

    def set_atribut(self,val1='', val2=0, val3=''):
        self.nama =val1
        self.nim=val2
        self.__prodi =val3

    def get_atribut(self):
        print("Nama \t:",self.nama,
              "\nNIM \t:",self.nim,
              "\nProdi\t:",self.__prodi)

mhs5 = Mahasiswa()
mhs5.set_atribut(val1='Furqan',val2=8080123)
mhs5.get_atribut()

mhs6 = Mahasiswa()
mhs6.set_atribut(val1='Farrah',val3='Farmasi')
mhs6.get_atribut()
