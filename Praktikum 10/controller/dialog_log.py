# from PyQt5 import QtWidgets
# from PyQt5.QtGui import QStandardItemModel, QStandardItem
#
# from ui.log import Ui_Dialog as TampilLog
# from model.User import User
#
# class Dialog_tampil_log(QtWidgets.QDialog, TampilLog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#
#         self.user = User()
#         self.tampil_tabel()
#
#     def tampil_tabel(self):
#         data = self.user.select_data_tabel_log()
#
#         self.model = QStandardItemModel()
#         self.model.setHorizontalHeaderLabels(["Tanggal & Jam", "User", "Keterangan"])
#         for row in data:
#             items = [QStandardItem(str(field)) for field in row]
#             self.model.appendRow(items)
#         self.tableView.setModel(self.model)



    