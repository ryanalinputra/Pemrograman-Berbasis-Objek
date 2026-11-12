import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = []
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Nama", "NIM"])
        for row in self.data:
            items = [QStandardItem(field) for field in row]
            self.model.appendRow(items)
        self.tableView.setModel(self.model)
        self.pushButton.clicked.connect(self.tambah_data)

    def tambah_data(self):
        nama = self.lineEdit.text()
        nim = self.lineEdit_2.text()
        if nim and nama:
            items = [QStandardItem(nama), QStandardItem(nim)]
            self.model.appendRow(items)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            print("NIM dan Nama harus diisi!")
            
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())