import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "T06_Cálculo del IVA de una cantidad dada.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.lnE1.setValidator(QDoubleValidator())
        self.lnE1.textChanged.connect(self.Validacion)
        self.btn1.clicked.connect(self.btnCalcular)

    # Area de los Slots
    def Validacion(self):
        if self.lnE1.text():
            self.btn1.setEnabled(True)
        else:
            self.btn1.setEnabled(False)

    def btnCalcular(self):
        num = float(self.lnE1.text())
        IVA = num*0.16
        mensaje = QMessageBox()
        mensaje.information(self, "Resultado", "El IVA es: " + str(IVA))
        self.lnE1.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())