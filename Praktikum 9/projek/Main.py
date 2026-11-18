import sys
from PyQt5 import QtWidgets
from skor import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_a.clicked.connect(self.timA)
        self.pushButton_b.clicked.connect(self.timB)
        self.pushButton_cek.clicked.connect(self.cek)
        self.pushButton_reset.clicked.connect(self.reset)

    def timA(self):
        skorA = int(self.skor_a.text())
        skorA += 1
        self.skor_a.setText(str(skorA))
    def timB(self):
        skorB = int(self.skor_b.text())
        skorB += 1
        self.skor_b.setText(str(skorB))
    
    def cek(self):
        skorA = int(self.skor_a.text())
        skorB = int(self.skor_b.text())
        if skorA > skorB:
            self.keterangan.setText("Tim A menang")
        elif skorA < skorB:
            self.keterangan.setText("Tim B menang")
        else:
            self.keterangan.setText("Seri")

    def reset(self):
        self.skor_a.setText("0")
        self.skor_b.setText("0")
        self.keterangan.setText("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())