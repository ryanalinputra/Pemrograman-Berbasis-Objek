from PyQt5 import QtWidgets
import sys

from ui.dashboard_kasir import Ui_MainWindow as KasirUI
from controller.dialog_kasir import Dialog_tambah_barang as TambahBarangUI
from controller.dialog_kasir import Dialog_ubah_barang as UbahBarangUI
from model.Barang import Barang

class HalamanKasir(QtWidgets.QMainWindow, KasirUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.barang = Barang()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nama", "Stok", "Harga", "Kategori"])
        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)

    def tampil_tabel(self):
        data = self.barang.select_data_tabel()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, val in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))
    
    def buka_form_tambah(self):
        dialog = TambahBarangUI()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def buka_form_ubah(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        id_barang = self.tableWidget.item(row, 0).text()
        nama = self.tableWidget.item(row, 1).text()
        stok = self.tableWidget.item(row, 2).text()
        harga = self.tableWidget.item(row, 3).text()
        kategori = self.tableWidget.item(row, 4).text()

        dialog = UbahBarangUI(id_barang, nama, stok, harga, kategori)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def konfirmasi_hapus(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        ID = self.tableWidget.item(row, 0).text()

        reply = QtWidgets.QMessageBox.question(None, "Konfirmasi", "Yakin akan menghapus data?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.barang.delete_data(ID)
            self.tampil_tabel()
    
    def kembali(self):
        reply = QtWidgets.QMessageBox.question(None, "Konfirmasi", "Yakin akan logout?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()