import sys
from PyQt5 import uic, QtWidgets, QtGui
import math
qtCreatorFile = "T05_Peso_a_Dolar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10000)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("1 MXN")
        self.btn_convertir.clicked.connect(self.convertir)

    def cambiaValor(self):
        value_mxn = self.horizontalSlider.value()
        self.txt_valor.setText(f"{value_mxn} MXN")

    def convertir(self):
        value_mxn = self.horizontalSlider.value()
        tasa_cambio = 21.27
        value_usd = value_mxn / tasa_cambio
        self.txt_resultado.setText(f"{value_usd:.2f} USD")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())