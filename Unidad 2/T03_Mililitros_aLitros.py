import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "T03_Mililitros_a_litros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(5000)
        self.verticalSlider.setSingleStep(100)
        self.verticalSlider.setValue(0)
        self.verticalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("0 ml")
        self.txt_litros.setText("0.00 L")

        self.btn_convertir.clicked.connect(self.convertir)

    def cambiaValor(self):
        value_ml = self.verticalSlider.value()
        self.txt_valor.setText(f"{value_ml} ml")

    def convertir(self):
        value_ml = self.verticalSlider.value()
        value_l = value_ml / 1000
        self.txt_litros.setText(f"{value_l:.2f} L")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())