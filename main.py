from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

ui=uic.loadUi("mainwindow.ui")

ui.show()

app.exec()