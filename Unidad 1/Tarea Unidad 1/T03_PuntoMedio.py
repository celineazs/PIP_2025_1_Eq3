import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "T03_PuntoMedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular_punto_medio)
    def calcular_punto_medio(self):
        try:
            ax = float(self.le_Ax.text())
            ay = float(self.le_Ay.text())
            bx = float(self.le_Bx.text())
            by = float (self.le_By.text())
            mx = (ax + bx) / 2
            my = (ay + by) / 2
            mensaje = f"El punto medio es:\n M ({mx}, {my})"
            self.mostrar_mensaje("Resultado", mensaje)
        except ValueError:
            self.mostrar_mensaje("Error", "Por favor, introduce valores numéricos válidos.")
    def mostrar_mensaje(self, titulo, mensaje):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(titulo)
        msg.setText(mensaje)
        msg.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
