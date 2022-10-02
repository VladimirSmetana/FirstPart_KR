from PyQt5 import QtWidgets
from form import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.progexit)

    def progexit(self):
        exit()
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())