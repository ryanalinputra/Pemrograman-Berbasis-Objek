from PyQt5 import QtWidgets

from ui.tambah_user import Ui_Dialog as TambahUserUI
from ui.ubah_user import Ui_Dialog as UbahUserUI
from model.User import User

class Dialog_tambah_user(QtWidgets.QDialog, TambahUserUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user = User()

        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def tambah_data(self):
        nama = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if self.radioButton.isChecked():
            level = "Admin"
        elif self.radioButton_2.isChecked():
            level = "Kasir"
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Pilih level!")
            return

        if not nama or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "Data tidak boleh kosong!")
            return

        self.user.insert_data(nama, username, password, level)
        self.accept()

class Dialog_ubah_user(QtWidgets.QDialog, UbahUserUI):
    def __init__(self, nama, username, password, level):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.setText(nama)
        self.lineEdit_2.setText(username)
        self.lineEdit_3.setText(password)
        if level == "Admin":
            self.radioButton.setChecked(True)
        else:
            self.radioButton_2.setChecked(True)
        
        self.user = User()
        self.pushButton.clicked.connect(self.ubah_data)
        self.pushButton_2.clicked.connect(self.reject)

    def ubah_data(self):
        nama = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if self.radioButton.isChecked():
            level = "Admin"
        elif self.radioButton_2.isChecked():
            level = "Kasir"

        self.user.update_data(nama, password, level, username)
        self.accept()

    