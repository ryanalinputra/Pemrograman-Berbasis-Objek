from PyQt5 import QtWidgets
import sys

from ui.kelola_kategori import Ui_MainWindow as KelolaKategoriUI
from controller.dialog_kategori import Dialog_tambah_kategori as TambahKategoriUI
from controller.dialog_kategori import Dialog_ubah_kategori as UbahKategoriUI
from model.Kategori import Kategori

class HalamanKelolaKategori(QtWidgets.QMainWindow, KelolaKategoriUI):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.kategori = Kategori()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Kategori"])
        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        self.pushButton_2.clicked.connect(self.buka_form_ubah)
        self.pushButton_3.clicked.connect(self.konfirmasi_hapus)
        self.pushButton_4.clicked.connect(self.kembali)

    def tampil_tabel(self):
        data = self.kategori.get_Data()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, val in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))

    def buka_form_tambah(self):
        dialog = TambahKategoriUI()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def buka_form_ubah(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        id_kategori = self.tableWidget.item(row, 0).text()
        nama = self.tableWidget.item(row, 1).text()

        dialog = UbahKategoriUI(id_kategori, nama)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def konfirmasi_hapus(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            QtWidgets.QMessageBox.warning(None, "Warning", "Pilih data dulu!")
            return

        ID = self.tableWidget.item(row, 0).text()

        reply = QtWidgets.QMessageBox.question(None, "Konfirmasi", "Yakin akan menghapus data?\nSemua barang berelasi akan ikut terhapus!", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.kategori.delete(ID)
            self.tampil_tabel()

    def kembali(self):
        self.close()
        if self.parent:
            self.parent.show()

    def closeEvent(self, event):
        if self.parent and not self.parent.isVisible():
            self.parent.show()
        event.accept()
