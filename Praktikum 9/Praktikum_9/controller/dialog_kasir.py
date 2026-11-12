from PyQt5 import QtWidgets

from ui.tambah_barang import Ui_Dialog as TambahBarangUI
from ui.ubah_barang import Ui_Dialog as UbahBarangUI
from model.Barang import Barang

class Dialog_tambah_barang(QtWidgets.QDialog, TambahBarangUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItems(["Obat Bebas", "Obat Bebas Terbatas", "Obat Keras", "Obat Herbal"])

        self.barang = Barang()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        id_barang = self.lineEdit.text()
        nama = self.lineEdit_2.text()
        stok = self.spinBox.value()
        harga = self.lineEdit_3.text()
        kategori = self.comboBox.currentText()

        self.barang.insert_data(id_barang ,nama, stok, harga, kategori)
        self.accept()

class Dialog_ubah_barang(QtWidgets.QDialog, UbahBarangUI):
    def __init__(self, id_barang ,nama, stok, harga, kategori):
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItems(["Obat Bebas", "Obat Bebas Terbatas", "Obat Keras", "Obat Herbal"])

        self.lineEdit.setText(id_barang)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setText(nama)
        self.spinBox.setValue(int(stok))
        self.lineEdit_3.setText(harga)
        self.comboBox.setCurrentText(kategori)
        
        self.barang = Barang()
        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        id_barang = self.lineEdit.text()
        nama = self.lineEdit_2.text()
        stok = self.spinBox.value()
        harga = self.lineEdit_3.text()
        kategori = self.comboBox.currentText()
            
        self.barang.update_data(nama, stok, harga, kategori, id_barang)
        self.accept()