from PyQt5 import QtWidgets
import sys

from ui.dashboard_kasir import Ui_MainWindow as KasirUI
from controller.kelola_barang import HalamanKelolaBarang
from controller.kelola_kategori import HalamanKelolaKategori

class HalamanKasir(QtWidgets.QMainWindow, KasirUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.buka_kelola_barang)
        self.pushButton_2.clicked.connect(self.buka_kelola_kategori)
        # self.pushButton_3.clicked.connect(self.kembali)

    def buka_kelola_barang(self):
        self.hide()
        self.halaman_barang = HalamanKelolaBarang(self)
        self.halaman_barang.show()

    def buka_kelola_kategori(self):
        self.hide()
        self.halaman_kategori = HalamanKelolaKategori(self)
        self.halaman_kategori.show()
