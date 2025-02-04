import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T01_Cambio de grados centigrados a Fahrenheit.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.vs.setMinimum(1)
        self.vs.setMaximum(100)
        self.vs.setSingleStep(5)
        self.vs.setValue(1) #valor inicial
        self.vs.valueChanged.connect(self.cambiaValor)
        self.txt_gc.setText("1")


        self.btn_calcular.clicked.connect(self.calcularConversion)

    def cambiaValor(self):
        valor=self.vs.value()
        self.txt_gc.setText(str(valor))


    def calcularConversion(self):
        gradosC = self.vs.value()
        gradosF = (gradosC * 9/5) + 32
        self.txt_gf.setText(str(gradosF))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())