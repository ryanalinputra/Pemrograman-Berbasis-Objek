import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton.toggled.connect(self.cek_no1)
        self.radioButton_2.toggled.connect(self.cek_no1)
        self.radioButton_3.toggled.connect(self.cek_no1)
        self.radioButton_4.toggled.connect(self.cek_no2)
        self.radioButton_5.toggled.connect(self.cek_no2)
        self.radioButton_6.toggled.connect(self.cek_no2)
        self.radioButton_7.toggled.connect(self.cek_no3)
        self.radioButton_8.toggled.connect(self.cek_no3)
        self.radioButton_9.toggled.connect(self.cek_no3)
    
    def cek_no1(self):
        if self.radioButton.isChecked():
            self.label.setText("Jawaban no 1 : A")
        elif self.radioButton_2.isChecked():
            self.label.setText("Jawaban no 1 : B")
        elif self.radioButton_3.isChecked():
            self.label.setText("Jawaban no 1 : C")
    def cek_no2(self):
        if self.radioButton_4.isChecked():
            self.label_2.setText("Jawaban no 2 : A")
        elif self.radioButton_5.isChecked():
            self.label_2.setText("Jawaban no 2 : B")
        elif self.radioButton_6.isChecked():
            self.label_2.setText("Jawaban no 2 : C")
    def cek_no3(self):
        if self.radioButton_7.isChecked():
            self.label_3.setText("Jawaban no 3 : A")
        elif self.radioButton_8.isChecked():
            self.label_3.setText("Jawaban no 3 : B")
        elif self.radioButton_9.isChecked():
            self.label_3.setText("Jawaban no 3 : C")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())