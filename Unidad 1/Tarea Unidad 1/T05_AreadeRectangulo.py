import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T05_AreadelRectangulo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcularareaR.clicked.connect(self.calcularareaR)

    # Área de los Slots
    def calcularareaR(self):
        try:
            base = float(self.txt_base.text())
            altura = float(self.txt_altura.text())
            calcularareaR = (base * altura)
            self.msj(f"El área del rectángulo es: {calcularareaR} cm²")
        except Exception as error:
            print(error)
    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())