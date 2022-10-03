from PyQt5 import QtWidgets
from form import Ui_MainWindow
import sys

class calclass():
    def start_calc(self):
        le = float(application.ui.le_edit.text())
        delta = float(application.ui.delta_edit.text())
        q = float(application.ui.q_edit.text())
        omega = float(application.ui.omega_edit.text())
        kf = float(application.ui.kf_edit.text())
        kd = float(application.ui.kd_edit.text())
        altitude = float(application.ui.Hlabel.text())

        #application.ui.lineEdit_14.setText(str(le+delta))


calculations = calclass()
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_button.clicked.connect(self.exit)
        self.ui.verticalSlider.valueChanged.connect(self.HlabelSet)
        self.ui.calc_button.clicked.connect(calculations.start_calc)
    def exit(self):
        exit()
    def HlabelSet(self):
        self.ui.Hlabel.setText(str(self.ui.verticalSlider.value()))




app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())