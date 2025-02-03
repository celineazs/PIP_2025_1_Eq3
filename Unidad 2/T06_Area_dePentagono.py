import sys
from PyQt5 import uic, QtWidgets, QtGui
import math
qtCreatorFile = "T06_Area_deun_Pentagono.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.dial.setMinimum(1)
        self.dial.setMaximum(100)
        self.dial.setSingleStep(1)
        self.dial.setValue(1)

        self.dial.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("1 m")

        self.btn_convertir.clicked.connect(self.convertir)

    def cambiaValor(self):
        value_lado = self.dial.value()
        self.txt_valor.setText(f"{value_lado} m")

    def convertir(self):
        value_lado = self.dial.value()
        area = (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * value_lado ** 2
        self.txt_area.setText(f"{area:.2f} m²")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())