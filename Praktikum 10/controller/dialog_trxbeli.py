from PyQt5 import QtWidgets, QtCore

from ui.tambah_trxbeli import Ui_Dialog as TambahTrxUI
from model.Transaksi import Transaksi, TransaksiPembelian, DetailTransaksi
from model.Barang import Barang

class Dialog_tambah_pembelian(QtWidgets.QDialog, TambahTrxUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.trx = Transaksi()
        self.pembelian = TransaksiPembelian()
        self.detail = DetailTransaksi()
        self.barang = Barang()
        self.dateEdit_tanggal.setCalendarPopup(True)
        self.dateEdit_tempo.setCalendarPopup(True)
        self.dateEdit_tanggal.setDate(QtCore.QDate.currentDate())
        self.dateEdit_tempo.setDate(QtCore.QDate.currentDate())
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Nama", "Qty", "Harga","Sub Total"])
        for mtd in ['Tunai','Transfer','QRIS']:
            self.comboBox_metode.addItem(mtd)
        for sts in ['Lunas','Belum Lunas']:
            self.comboBox_status.addItem(sts)
        for brg in self.barang.select_data_tabel():
            self.comboBox_barang.addItem(f"{brg[0]} - {brg[1]}")
        self.set_harga()

        self.comboBox_barang.activated.connect(self.set_harga)
        self.pushButton_tambah_item.clicked.connect(self.tambah_item)
        self.pushButton_simpan.clicked.connect(self.simpan)
        self.pushButton_batal.clicked.connect(self.reject)

    def set_harga(self):
        barang = self.comboBox_barang.currentText()
        id_barang = barang.split(" - ")[0]
        harga = int(self.barang.select_harga(id_barang))
        self.lineEdit_harga.setText(str(harga))

    def tambah_item(self):
        barang = self.comboBox_barang.currentText()
        id_barang = barang.split(" - ")[0]
        nama = barang.split(" - ")[1]
        qty = self.spinBox_qty.value()
        harga = int(self.lineEdit_harga.text())
        subtotal = qty * harga

        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(id_barang))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(nama))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(qty)))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(harga)))
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(subtotal)))

        self.hitung_total()

    def hitung_total(self):
        total = 0
        for row in range(self.tableWidget.rowCount()):
            subtotal_item = int(self.tableWidget.item(row, 4).text())
            total += subtotal_item
        self.lineEdit_total.setText(str(total))

    def simpan(self):
        tanggal = self.dateEdit_tanggal.date().toString("yyyy-MM-dd")
        supplier = self.lineEdit_supplier.text()
        faktur = self.lineEdit_faktur.text()
        metode = self.comboBox_metode.currentText()
        tempo = self.dateEdit_tempo.date().toString("yyyy-MM-dd")
        status = self.comboBox_status.currentText()
        id_trx = self.trx.insert_data(tanggal, "pembelian")

        for row in range(self.tableWidget.rowCount()):
            id_barang = self.tableWidget.item(row, 0).text()
            qty = int(self.tableWidget.item(row, 2).text())
            harga = int(self.tableWidget.item(row, 3).text())
            subtotal = int(self.tableWidget.item(row, 4).text())

            self.detail.insert_data(id_trx, id_barang, qty, harga, subtotal)

        self.pembelian.insert_data(id_trx, supplier, faktur, metode, tempo, status)
        self.accept()
