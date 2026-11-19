from PyQt5 import QtWidgets
import sys

from ui.kelola_barang import Ui_MainWindow as KelolaBarangUI
from controller.dialog_barang import Dialog_tambah_barang as TambahBarangUI
from controller.dialog_barang import Dialog_ubah_barang as UbahBarangUI
from model.Barang import Barang

class HalamanKelolaBarang(QtWidgets.QMainWindow, KelolaBarangUI):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.barang = Barang()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nama", "Stok", "Harga", "Kategori"])
        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)

    def tampil_tabel(self):
        data = self.barang.select_all()
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
        data = self.barang.select_by_id(id_barang)
        if data:
            kode = data[0]
            nama = data[1]
            stok = data[2]
            harga = data[3]
            kategori = data[4]

            dialog = UbahBarangUI(kode, nama, stok, harga, kategori)
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
            self.barang.delete(ID)
            self.tampil_tabel()

    def kembali(self):
        self.close()
        if self.parent:
            self.parent.show()

    def closeEvent(self, event):
        if self.parent and not self.parent.isVisible():
            self.parent.show()
        event.accept()
