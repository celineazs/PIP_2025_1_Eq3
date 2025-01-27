import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T02_Mts_a_Pies.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular_pies)

    def calcular_pies(self):
        try:
            metros = float(self.le_Metros.text())

            if metros < 0:
                self.mostrar_mensaje("Error", "El valor en metros no puede ser negativo.")
                return
            pies = metros * 3.28084
            mensaje = f"{metros} metros son {pies:.2f} pies."
            self.mostrar_mensaje("Resultado", mensaje)
        except ValueError:
            self.mostrar_mensaje("Error", "Por favor, introduce un valor numérico válido.")
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
