import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.klik_button_a)
        self.pushButton_2.clicked.connect(self.klik_button_b)
    
    def klik_button_a(self):
        self.label.setText("Button yang Anda pilih: A")
    def klik_button_b(self):
        self.label.setText("Button yang Anda pilih: B")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())