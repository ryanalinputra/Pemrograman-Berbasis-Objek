class AkunBank:
    def __init__(self, nama, saldo=0):
        self.nama = nama
        self.__saldo = saldo

    def lihat_saldo(self):
        print(f"Saldo {self.nama}: {self.__saldo}")

    def setor_uang(self, jumlah):
        self.__saldo += jumlah
        print(f"{self.nama}Setor uang berhasil. Saldo saat ini: {self.__saldo}")

akun1 = AkunBank('Budi')
akun1.lihat_saldo()

akun2 = AkunBank('Rama')
akun2.lihat_saldo()

akun1.setor_uang(100000)
akun1.lihat_saldo()
akun2.setor_uang(100000)
akun2.lihat_saldo()

