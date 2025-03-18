import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t

import P2_vPython_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_suma.clicked.connect(self.suma)

    def suma(self):
        a= int(self.txt_num1.text())
        b= int(self.txt_num2.text())
        c= int(self.txt_num3.text())
        s=a+b+c
        self.msj("La suma es: " + str(s))

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())