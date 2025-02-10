import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E12_Simon_dice.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.diccionarioDatos = {
            1: ":/Ejercicios/tata.jpg",
            2: ":/Ejercicios/cooky.jpg",
            3: ":/Ejercicios/rj.jpg",
            4: ":/Ejercicios/chimmy.jpg"
        }

        self.btn_1.clicked.connect(self.verificarSeleccion)
        self.btn_2.clicked.connect(self.verificarSeleccion)
        self.btn_3.clicked.connect(self.verificarSeleccion)
        self.btn_4.clicked.connect(self.verificarSeleccion)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mostrarImagen)

        self.patronMemorizado = []
        self.imagen_actual = 0
        self.eleccion_usuario = []

        self.iniciarJuego()

    def iniciarJuego(self):
        self.msj("Memoriza la secuencia de imágenes.")

        self.patronMemorizado = [random.randint(1, 4) for _ in range(3)]
        self.imagen_actual = 0
        self.eleccion_usuario = []
        self.Botones(False)
        self.timer.start(1000)

    def mostrarImagen(self):
        if self.imagen_actual < len(self.patronMemorizado):
            img_id = self.patronMemorizado[self.imagen_actual]
            self.lbl_imagen.setPixmap(QtGui.QPixmap(self.diccionarioDatos[img_id]))
            self.imagen_actual += 1
        else:
            self.timer.stop()
            self.msj("Selecciona la secuencia en el orden correcto.")
            self.Botones(True)

    def verificarSeleccion(self):
        boton_presionado = self.sender()
        boton_numero = {
            self.btn_1: 1,
            self.btn_2: 2,
            self.btn_3: 3,
            self.btn_4: 4
        }

        self.eleccion_usuario.append(boton_numero[boton_presionado])

        if self.eleccion_usuario != self.patronMemorizado[:len(self.eleccion_usuario)]:
            self.msj("Incorrecto :( , inténtalo de nuevo.")
            self.iniciarJuego()
            return

        if len(self.eleccion_usuario) == len(self.patronMemorizado):
            self.msj("¡¡Correcto!! Se iniciará un nuevo patrón.")
            self.iniciarJuego()

    def Botones(self, estado):
        self.btn_1.setEnabled(estado)
        self.btn_2.setEnabled(estado)
        self.btn_3.setEnabled(estado)
        self.btn_4.setEnabled(estado)

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

