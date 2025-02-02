import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_Componente_Horizontalslider_Ejemplo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(-50) #valor inicial
        self.horizontalSlider.valueChanged.connect(self.cambiaValor)
        self.txt_valor.setText("-50")


    def cambiaValor(self):
        value=self.horizontalSlider.value()
        self.txt_valor.setText(str(value))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())