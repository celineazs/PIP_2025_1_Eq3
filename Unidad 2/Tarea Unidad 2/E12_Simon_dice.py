import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore

qtCreatorFile = "E12_Simon_dice.ui"  # Archivo .ui con la interfaz
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Diccionario de imágenes
        self.diccionarioDatos = {
            1: ":/Ejercicios/tata.jpg",
            2: ":/Ejercicios/cooky.jpg",
            3: ":/Ejercicios/rj.jpg",
            4: ":/Ejercicios/chimmy.jpg"
        }

        # Botones y señales
        self.btn_1.clicked.connect(self.verificarSeleccion)
        self.btn_2.clicked.connect(self.verificarSeleccion)
        self.btn_3.clicked.connect(self.verificarSeleccion)
        self.btn_4.clicked.connect(self.verificarSeleccion)

        # Temporizador para mostrar secuencia
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mostrarSiguienteImagen)

        # Variables del juego
        self.patronMemorizado = []  # Lista del patrón mostrado
        self.indice_actual = 0  # Índice de la secuencia actual
        self.eleccion_usuario = []  # Lista de elecciones del usuario

        self.iniciarJuego()

    def iniciarJuego(self):
        """Inicia un nuevo patrón de memorización."""
        self.msj("Memoriza la secuencia de imágenes.")

        # Generar un patrón aleatorio de 3 imágenes
        self.patronMemorizado = [random.randint(1, 4) for _ in range(3)]
        self.indice_actual = 0
        self.eleccion_usuario = []  # Limpiar elecciones previas

        # Deshabilitar botones mientras se muestra la secuencia
        self.habilitarBotones(False)

        # Iniciar el temporizador para mostrar la secuencia
        self.timer.start(1000)

    def mostrarSiguienteImagen(self):
        """Muestra la secuencia de imágenes una por una."""
        if self.indice_actual < len(self.patronMemorizado):
            img_id = self.patronMemorizado[self.indice_actual]
            self.lbl_imagen.setPixmap(QtGui.QPixmap(self.diccionarioDatos[img_id]))
            self.indice_actual += 1
        else:
            # Termina la secuencia y habilita la selección del usuario
            self.timer.stop()
            self.msj("Ahora selecciona la secuencia en el orden correcto.")
            self.habilitarBotones(True)

    def verificarSeleccion(self):
        """Verifica si la secuencia elegida por el usuario es correcta."""
        boton_presionado = self.sender()

        # Mapear botones a valores
        boton_a_numero = {
            self.btn_1: 1,
            self.btn_2: 2,
            self.btn_3: 3,
            self.btn_4: 4
        }

        self.eleccion_usuario.append(boton_a_numero[boton_presionado])

        # Verificar si la secuencia elegida es correcta hasta ahora
        if self.eleccion_usuario != self.patronMemorizado[:len(self.eleccion_usuario)]:
            self.msj("Incorrecto. Inténtalo de nuevo.")
            self.iniciarJuego()  # Reiniciar el juego
            return

        # Si el usuario completó toda la secuencia correctamente
        if len(self.eleccion_usuario) == len(self.patronMemorizado):
            self.msj("¡Correcto! Se iniciará un nuevo patrón.")
            self.iniciarJuego()

    def habilitarBotones(self, estado):
        """Habilita o deshabilita los botones de selección."""
        self.btn_1.setEnabled(estado)
        self.btn_2.setEnabled(estado)
        self.btn_3.setEnabled(estado)
        self.btn_4.setEnabled(estado)

    def msj(self, txt):
        """Muestra un mensaje emergente."""
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

