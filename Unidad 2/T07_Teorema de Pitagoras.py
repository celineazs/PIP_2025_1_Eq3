import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T07_Teorema de Pitagoras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hs_co.setMinimum(1)
        self.hs_co.setMaximum(100)
        self.hs_co.setSingleStep(5)
        self.hs_co.setValue(1) #valor inicial
        self.hs_co.valueChanged.connect(self.cambiaValor)
        self.txt_catetoO.setText("1")

        self.hs_ca.setMinimum(1)
        self.hs_ca.setMaximum(100)
        self.hs_ca.setSingleStep(5)
        self.hs_ca.setValue(1)  # valor inicial
        self.hs_ca.valueChanged.connect(self.cambiaValor)
        self.txt_catetoA.setText("1")

        self.btn_calcular.clicked.connect(self.calcularHipotenusa)

    def cambiaValor(self):
        value1=self.hs_co.value()
        self.txt_catetoO.setText(str(value1))
        value2=self.hs_ca.value()
        self.txt_catetoA.setText(str(value2))

    def calcularHipotenusa(self):
        catetoO = self.hs_co.value()
        catetoA = self.hs_ca.value()
        hipotenusa = (catetoO**2 + catetoA**2)**0.5
        self.txt_hipotenusa.setText(str(hipotenusa))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())