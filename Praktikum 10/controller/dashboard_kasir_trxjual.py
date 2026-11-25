from PyQt5 import QtWidgets
import sys

from ui.dashboard_kasir_trxjual import Ui_MainWindow as PenjualanUI
from controller.dialog_trxjual import Dialog_tambah_penjualan as TambahUI
from model.Transaksi import Transaksi, TransaksiPenjualan

class HalamanPenjualan(QtWidgets.QMainWindow, PenjualanUI):
    def __init__(self, app_controller=None):
        super().__init__()
        self.setupUi(self)
        self.app_controller = app_controller

        self.trx = Transaksi()
        self.penjualan = TransaksiPenjualan()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID","Tanggal", "Pelanggan", "Diskon", "Metode Bayar", "Bayar", "Kembalian"
        ])

        self.tampil_tabel()

        self.pushButton.clicked.connect(self.buka_form_tambah)
        if self.app_controller:
            self.pushButton_4.clicked.connect(self.app_controller.logout)
        else:
            self.pushButton_4.clicked.connect(self.kembali)
        self.actionBarang.triggered.connect(self.buka_dashboard_barang)
        self.actionTransaksi_Pembelian.triggered.connect(self.buka_dashboard_trxbeli)

    def tampil_tabel(self):
        data = self.trx.select_data_trxjual()
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, val in enumerate(row_data):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(val)))

    def buka_form_tambah(self):
        dialog = TambahUI()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.tampil_tabel()

    def kembali(self):
        reply = QtWidgets.QMessageBox.question(
            None,
            "Konfirmasi",
            "Yakin ingin logout?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            self.close()

    def buka_dashboard_barang(self):
        from controller.dashboard_kasir import HalamanKasir as KasirUI
        self.window_pembelian = KasirUI(self.app_controller)
        if self.app_controller:
            self.app_controller.window = self.window_pembelian
        self.window_pembelian.show()
        self.close()

    def buka_dashboard_trxbeli(self):
        from controller.dashboard_kasir_trxbeli import HalamanPembelian as KasirBeliUI
        self.window_pembelian = KasirBeliUI(self.app_controller)
        if self.app_controller:
            self.app_controller.window = self.window_pembelian
        self.window_pembelian.show()
        self.close()
