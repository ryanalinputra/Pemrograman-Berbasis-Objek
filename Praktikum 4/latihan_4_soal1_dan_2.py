class Kendaraan:
    def __init__(self):
        self._jenis = ""
        self._merk = ""
        self._nama = ""
        self._warna = ""

    def set_atribut(self,val1 ='',val2='',val3='',val4=''):
        self._jenis = val1
        self._merk = val2
        self._nama = val3
        self._warna = val4

    def get_atribut(self):
        print("Jenis \t:",self._jenis,
              "\nMerk \t:",self._merk,
              "\nNama \t:",self._nama,
              "\nWarna\t:",self._warna)


mobil = Kendaraan()
mobil.set_atribut(val1='Toyota',val2='Inova',val3='Inova Reborn',val4='Hitam')
mobil.get_atribut()

mobil2 = Kendaraan()
mobil2.set_atribut(val3='brio',val4='Merah')
mobil2.get_atribut()

motor = Kendaraan()
motor.set_atribut(val2='Honda',val3='vario',val4='Hitam')
motor.get_atribut()

