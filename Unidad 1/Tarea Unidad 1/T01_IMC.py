import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "T01_IMC.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Calcular.clicked.connect(self.calcular_imc)
    def calcular_imc(self):
        try:
            estatura = float(self.le_Estatura.text())
            peso = float(self.le_Peso.text())
            if estatura <= 0:
                self.mostrar_mensaje("Error", "La estatura debe ser mayor que cero.")
                return
            imc = peso / (estatura ** 2)
            nivel_peso = self.obtener_nivel_peso(imc)
            mensaje = f"Tu IMC es: {imc:.2f}\nNivel de peso: {nivel_peso}"
            self.mostrar_mensaje("Resultado", mensaje)
        except ValueError:
            self.mostrar_mensaje("Error", "Introduce valores numéricos válidos.")
    def obtener_nivel_peso(self, imc):
        # Clasificación del nivel de peso
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            return "Peso saludable"
        elif 25.0 <= imc <= 29.9:
            return "Sobrepeso"
        else:
            return "Obesidad"
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
