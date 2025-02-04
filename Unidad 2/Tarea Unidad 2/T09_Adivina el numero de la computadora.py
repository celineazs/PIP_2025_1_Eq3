import sys
from random import random, randint
from PyQt5 import uic, QtWidgets

qtCreatorFile = "T09_Adivina el numero de la computadora.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hs.setMinimum(1)
        self.hs.setMaximum(100)
        self.hs.setSingleStep(5)
        self.hs.setValue(1) #valor inicial
        self.hs.valueChanged.connect(self.cambiaValor)
        self.txt_num.setText("1")
        self.numaleatorio = randint(1,100)
        self.btn_calcular.clicked.connect(self.adivinarelnumero)

    def cambiaValor(self):
        num=self.hs.value()
        self.txt_num.setText(str(num))


    def adivinarelnumero(self):
        num = self.hs.value()
        if num == self.numaleatorio:
            self.msj("Felicidades, adivinaste el número")
        elif num < self.numaleatorio:
            self.msj("El número que buscas es mayor")
        else:
            self.msj("El número que buscas es menor")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Mensaje")
        m.setText(txt)
        m.exec_()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())