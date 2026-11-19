from PyQt5 import QtWidgets

from ui.tambah_kategori import Ui_Dialog as TambahKategoriUI
from ui.ubah_kategori import Ui_Dialog as UbahKategoriUI
from model.Kategori import Kategori

class Dialog_tambah_kategori(QtWidgets.QDialog, TambahKategoriUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kategori = Kategori()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        id_kategori = self.lineEdit.text()
        kategori = self.lineEdit_2.text()

        if not id_kategori or not kategori:
            QtWidgets.QMessageBox.warning(self, "Error", "Data tidak boleh kosong!")
            return

        self.kategori.insert(id_kategori, kategori)
        self.accept()

class Dialog_ubah_kategori(QtWidgets.QDialog, UbahKategoriUI):
    def __init__(self, id_kategori, kategori):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.setText(id_kategori)
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setText(kategori)
        
        self.kategori = Kategori()
        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        id_kategori = self.lineEdit.text()
        kategori = self.lineEdit_2.text()

        if not kategori:
            QtWidgets.QMessageBox.warning(self, "Error", "Data tidak boleh kosong!")
            return

        self.kategori.update(kategori, id_kategori)
        self.accept()
