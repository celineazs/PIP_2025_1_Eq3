import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(3)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1) #valor inicial
        self.selectorImagen.valueChanged.connect(self.cambiaValor)
        #self.txt_valor.setText("1")

        self.diccionarDatos = {
            1: ("C:\PIP_2025_1_Eq3\Archivos\Resources\Finalizada.png", ["Puño", "5 dedos", "BTS"]),
            2: ("C:\PIP_2025_1_Eq3\Archivos\Resources\Jungkook.jpg", ["Mano", "5 dedos", "BTS"]),
            3: ("C:\PIP_2025_1_Eq3\Archivos\Resources\Finalizada.png", ["Manopla", "5 dedos", "BTS"])

        }
        self.indice = 1
        self.obtenerDatos()


    def cambiaValor(self):
        self.indice =self.selectorImagen.value()
        self.ObtenerDatos()
        #self.txt_valor.setText(str(value))


    def obtenerDatos(self):
        nombre =self.diccionarDatos[self.indice][1][0]
        edad =self.diccionarDatos[self.indice][1][1]
        grupo =self.diccionarDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_grupo.setText(grupo)
        self.imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarDatos[self.indice][0]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())