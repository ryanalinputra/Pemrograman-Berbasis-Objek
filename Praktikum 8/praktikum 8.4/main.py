import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hitung)
    
    def hitung(self):
        try:
            angka1 = float(self.lineEdit.text())
            angka2 = float(self.lineEdit_2.text())
            hasil = angka1 + angka2
            self.label_3.setText(str(hasil))
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowsTitle("Kesalahan Input")
            msg.setText("Input harus berupa angka!")
            msg.setStandarButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())