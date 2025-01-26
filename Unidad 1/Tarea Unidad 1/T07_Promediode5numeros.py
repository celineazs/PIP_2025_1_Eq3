import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T07_Promedio5numeros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_calcularpromedio.clicked.connect(self.calcularpromedio)

    # Promedio de los Slots
    def calcularpromedio(self):
        try:
            # Obtén los valores ingresados por el usuario y conviértelos a enteros
            numero1 = float(self.txt_n1.text())
            numero2 = float(self.txt_n2.text())
            numero3 = float(self.txt_n3.text())
            numero4 = float(self.txt_n4.text())
            numero5 = float(self.txt_n5.text())
            calcularpromedio = (numero1 + numero2 + numero3 + numero4 + numero5) / 5
            self.msj(f"El promedio es: {calcularpromedio}")
        except Exception as error:
            self.msj(f"Error: {error}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
