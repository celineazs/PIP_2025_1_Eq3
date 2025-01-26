import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "T08_Cálculo de la velocidad dada una distancia y tiempo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.lnE1.setValidator(QDoubleValidator())
        self.lnE1.textChanged.connect(self.Validacion)
        self.lnE2.setValidator(QDoubleValidator())
        self.lnE2.textChanged.connect(self.Validacion)
        self.btn1.clicked.connect(self.btnCalcular)

    # Area de los Slots
    def Validacion(self):
        if self.lnE1.text() and self.lnE2.text():
            self.btn1.setEnabled(True)
        else:
            self.btn1.setEnabled(False)

    def btnCalcular(self):
        num1 = float(self.lnE1.text())
        num2 = float(self.lnE2.text())
        velocidad = num1 / num2
        mensaje = QMessageBox()
        mensaje.information(self, "Resultado", "La Velocidad es: " + str(velocidad) + " m/s")
        self.lnE1.clear()
        self.lnE2.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())