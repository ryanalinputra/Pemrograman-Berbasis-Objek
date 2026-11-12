import sys
from PyQt5 import QtWidgets
from desain import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tampilkan_text)
    
    def tampilkan_text(self):
        text = self.lineEdit.text()
        self.label.setText(text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())