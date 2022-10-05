# pyuic5 mainwindow.ui -o form.py
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from form import Ui_MainWindow
import sys
import math

class calclass():

    def rad(self,arg):
        return math.pi*arg/180
    def deg(self,arg):
        return 180*arg/math.pi

    def start_calc(self):
        alt = float(application.ui.Hlabel.text())
        w= float(application.ui.omega_edit.text())
        w = self.rad(w)
        lrme = float(application.ui.le_edit.text())
        lp = float(application.ui.pic_edit.text())
        q = float(application.ui.q_edit.text())
        delta = float(application.ui.delta_edit.text())
        kf = float(application.ui.kf_edit.text())
        kd = float(application.ui.kd_edit.text())

        B=alt * math.tan(w)
        p=alt+6371
        T= 2 * math.pi * math.sqrt((p**3)/398600)
        N = 86400 / T
        i = math.acos((398600*pow(p, 2)*(2*math.pi-86400*0.7292115*pow(10, -4)))/(2*math.pi*2.634*pow(10,10)*N))
        i = self.deg(i)
        dmin =  0.00000055 * alt * 1000 * 1.1 / (2 * 0.3 * lrme)
        fekv = 0.734 * dmin * lp * pow(10, -6) / 0.00000055
        dvz = dmin * q
        d = q * fekv - delta
        s2 = d * q / (1 - q)
        fgz = d + s2
        fvz = (q * fekv * (-delta + q * fekv)) / (delta + fekv * (1 - 2 * q))
        rvz = 2 * fvz
        rgz = 2 * fgz
        m = fekv / fgz
        d1 = fgz * math.tan(w)
        d2 = m * d1
        ltk = fekv * kf
        dtk = dmin * kd


        B = round(B,3)
        p = round(p,3)
        T = round(T,3)
        N = round(N,3)
        i = round(i,3)
        dmin = round(dmin,3)
        fekv = round(fekv,3)
        dvz = round(dvz,3)
        d = round(d,3)
        s2 = round(s2,3)
        fgz = round(fgz,3)
        fvz = round(fvz,3)
        rgz = round(rgz,3)
        rvz =round(rvz,3)
        m = round(m,3)
        d1 = round(d1,3)
        d2 = round(d2,3)
        ltk = round(ltk,3)
        dtk = round(dtk,3)


        application.ui.BEdit_7.setText(str(B))
        application.ui.pEdit_9.setText(str(p))
        application.ui.TEdit_10.setText(str(T))
        application.ui.NEdit_12.setText(str(N))
        application.ui.iEdit_13.setText(str(i))
        application.ui.DminEdit_14.setText(str(dmin))
        application.ui.fekvEdit_11.setText(str(fekv))
        application.ui.DvzEdit_17.setText(str(dvz))
        application.ui.dEdit_18.setText(str(d))
        application.ui.s2Edit_19.setText(str(s2))
        application.ui.fvzEdit_16.setText(str(fvz))
        application.ui.rvzEdit_8.setText(str(rvz))
        application.ui.frzEdit_15.setText(str(fgz))
        application.ui.rgzEdit_20.setText(str(rgz))
        application.ui.iEdit_13.setText(str(i))
        application.ui.mEdit_21.setText(str(m))
        application.ui.d1Edit_22.setText(str(d1))
        application.ui.d2Edit_23.setText(str(d2))
        application.ui.LtkEdit_24.setText(str(ltk))
        application.ui.DtkEdit_25.setText(str(dtk))

calculations = calclass()
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        pix1 = QPixmap("images/1.jpg")
        pix2 = QPixmap("images/2.jpg")
        self.ui.img_1.setPixmap(pix1.scaled(300, 300))
        self.ui.img_2.setPixmap(pix2.scaled(300, 200))
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