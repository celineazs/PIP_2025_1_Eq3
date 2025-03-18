import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "E14_Ahorcado.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.diccionarDatos = {
            1: (r":Ejercicios\koya.jpg", "koya"),
            2: (r":Ejercicios\chimmy.jpg", "chimmy"),
            3: (r":Ejercicios\rj.jpg", "rj"),
            4: (r":Ejercicios\cooky.jpg", "cooky"),
            5: (r":Ejercicios\spiderman.jpg", "spiderman"),
            6: (r":Ejercicios\superman.jpg", "superman"),
            7: (r":Ejercicios\batman.jpg", "batman"),
            8: (r":Ejercicios\flash.jpg", "flash"),
        }

        self.indice = 1
        self.intentos = 6
        self.letras_adivinadas = []

        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(len(self.diccionarDatos))
        self.SelectorImagen.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)

        self.btn_adivinar.clicked.connect(self.adivinarLetra)

        self.obtenerDatos()

    def cambiaValor(self):
        self.indice = self.SelectorImagen.value()
        self.letras_adivinadas = []
        self.intentos = 6
        self.obtenerDatos()

    def obtenerDatos(self):
        imagen, palabra = self.diccionarDatos[self.indice]
        self.imagen_ahorcado.setPixmap(QtGui.QPixmap(imagen))
        self.txt_estado.setText(f"Intentos restantes: {self.intentos}")
        self.palabra_oculta = "".join(["_" if letra not in self.letras_adivinadas else letra for letra in palabra])
        self.txt_palabra.setText(" ".join(self.palabra_oculta))

    def adivinarLetra(self):
        letra = self.txt_letra.text().lower()

        if letra in self.diccionarDatos[self.indice][1] and letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
        else:
            self.intentos -= 1

        self.obtenerDatos()

        if self.intentos == 0:
            self.txt_estado.setText("¡Perdiste! El ahorcado está completo.")
        elif "_" not in self.palabra_oculta:
            self.txt_estado.setText("¡Ganaste! Has adivinado la palabra.")

        self.txt_letra.clear()
        self.txt_letra.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
