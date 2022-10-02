from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])

ui=uic.LoadUI("mainwindow.ui")

ui.show()

app.exec()