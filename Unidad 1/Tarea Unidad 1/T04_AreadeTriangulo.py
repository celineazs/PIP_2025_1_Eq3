import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T04_AreadelTriangulo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcularareaT.clicked.connect(self.calcularareaT)

    # Área de los Slots
    def calcularareaT(self):
        try:
            base = float(self.txt_base.text())
            calcularareaT = float(self.txt_altura.text())
            calcularareaT= (base * calcularareaT) / 2
            self.msj(f"El área del triángulo es: {calcularareaT} cm²")
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
