import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(3)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarDatos = {
            1: (":/Archivos/Resources/koya.jpg", ["Koya", "azul", "koala"]),
            2: (":/Archivos/Resources/cooky.jpg", ["Cooky", "rosa", "conejo"]),
            3: (":/Archivos/Resources/rj.jpg", ["Rj", "blanco", "alpaca"])
        }
        self.indice = 1
        self.obtenerDatos()


    def cambiaValor(self):
        self.indice = self.SelectorImagen.value()
        self.obtenerDatos()


    def obtenerDatos(self):
        nombre =self.diccionarDatos[self.indice][1][0]
        color =self.diccionarDatos[self.indice][1][1]
        forma =self.diccionarDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_color.setText(color)
        self.txt_forma.setText(forma)
        self.imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarDatos[self.indice][0]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())