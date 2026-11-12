import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.toggled.connect(self.cek_jawaban)
        self.radioButton_2.toggled.connect(self.cek_jawaban)
        self.radioButton_3.toggled.connect(self.cek_jawaban)
    
    def cek_jawaban(self):
        if self.radioButton.isChecked():
            self.label.setText("Jawaban Anda : A")
        elif self.radioButton_2.isChecked():
            self.label.setText("Jawaban Anda : B")
        elif self.radioButton_3.isChecked():
            self.label.setText("Jawaban Anda : C")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())