import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "E17_Simulador_Semaforo.ui"  # Nombre del archivo .ui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(3)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarDatos = {
            1: ":/Ejercicios/rojo.png",  # Imagen para el semáforo rojo
            2: ":/Ejercicios/amarillo.png",  # Imagen para el semáforo amarillo
            3: ":/Ejercicios/verde.png"  # Imagen para el semáforo verde
        }

        # Establecer el valor inicial para cambiar la imagen
        self.cambiaValor()

    def cambiaValor(self):
        indice = self.SelectorImagen.value()
        ruta_imagen = self.diccionarDatos[indice]
        self.lbl_imagen.setPixmap(QtGui.QPixmap(ruta_imagen))

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

