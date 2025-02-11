import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "PP02_CompuertasLogicas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(2)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)
        self.SelectorImagen_2.setMinimum(1)
        self.SelectorImagen_2.setMaximum(2)
        self.SelectorImagen_2.setSingleStep(1)
        self.SelectorImagen_2.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)
        self.SelectorImagen_2.valueChanged.connect(self.cambiaValor)
        self.btn_and.clicked.connect(self.acciones)
        self.btn_or.clicked.connect(self.acciones)


        self.diccionarDatos = {
            1: ":/Ejercicios/spiderman.jpg",
            2: ":/Ejercicios/superman.jpg",
        }

        self.cambiaValor()


    def cambiaValor(self):
        indice = self.SelectorImagen.value()
        ruta_imagen = self.diccionarDatos[indice]
        self.lbl_imagen.setPixmap(QtGui.QPixmap(ruta_imagen))
        indice2 = self.SelectorImagen_2.value()
        ruta_imagen2 = self.diccionarDatos[indice2]
        self.lbl_imagen_2.setPixmap(QtGui.QPixmap(ruta_imagen2))

    def acciones(self):
        indice = self.SelectorImagen.value()
        indice2 = self.SelectorImagen_2.value()
        boton_presionado = self.sender()
        if boton_presionado == self.btn_and:
            if indice == 1 & indice2 == 1:
                self.msj("0")
            elif indice == 2 & indice2 == 2:
                self.msj("1")
            else:
                    self.msj("0")
        if boton_presionado == self.btn_or:
            if indice == 1 & indice2 == 1:
                self.msj("0")
            elif indice == 2 & indice2 == 2:
                self.msj("1")
            else:
                    self.msj("1")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())