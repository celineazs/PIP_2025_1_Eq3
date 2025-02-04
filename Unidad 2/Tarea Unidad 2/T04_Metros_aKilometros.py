import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "T04_Metros_a_Kilometros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("0 m")
        self.txt_Kilometros.setText("0.00 km")

        self.btn_convertir.clicked.connect(self.convertir)

    def cambiaValor(self):
        value_m = self.horizontalSlider.value()
        self.txt_valor.setText(f"{value_m} m")

    def convertir(self):
        value_m = self.horizontalSlider.value()
        value_km = value_m / 1000
        self.txt_Kilometros.setText(f"{value_km:.2f} km")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())