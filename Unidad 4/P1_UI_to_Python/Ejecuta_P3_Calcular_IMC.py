import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t

import P3_vPython_Calcular_IMC as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.btn_calcular.clicked.connect(self.calcular)

        def calcular_imc(self):
            altura = float (self.txt_altura.text())
            peso = float(self.txt_peso.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())