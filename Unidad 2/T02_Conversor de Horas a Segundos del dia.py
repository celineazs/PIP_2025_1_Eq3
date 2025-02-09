import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T02_Conversor de Horas a Segundos del dia.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.vs.setMinimum(1)
        self.vs.setMaximum(24)
        self.vs.setSingleStep(1)
        self.vs.setValue(1) #valor inicial
        self.vs.valueChanged.connect(self.cambiaValor)
        self.txt_horas.setText("1:00")
        self.btn_calcular.clicked.connect(self.calcularHorasaSegundos)

    def cambiaValor(self):
        valor=self.vs.value()
        self.txt_horas.setText(f"{valor} : 00")


    def calcularHorasaSegundos(self):
        horas = self.vs.value()
        segundos = horas * 3600
        self.txt_segundos.setText(str(segundos))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())