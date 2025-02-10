import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "E18_SeleccionarOpcion.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.SelectorImagen.setMinimum(1)
        self.SelectorImagen.setMaximum(4)
        self.SelectorImagen.setSingleStep(1)
        self.SelectorImagen.setValue(1)
        self.SelectorImagen.valueChanged.connect(self.cambiaValor)
        self.btn_1.clicked.connect(self.identificarDino)
        self.btn_2.clicked.connect(self.identificarDino)
        self.btn_3.clicked.connect(self.identificarDino)
        self.btn_4.clicked.connect(self.identificarDino)

        self.diccionarDatos = {
            1: ":/Ejercicios/Carcharodontosaurus.jpeg",
            2: ":/logos/chubby-t-rex_1024.jpeg",
            3: ":/Ejercicios/Spinosaurus_aegyptiacus.jpeg",
            4: ":/logos/suchomimus-tenerensis-v0-jsm80tahvjic1.jpeg"
        }

        self.cambiaValor()


    def cambiaValor(self):
        indice = self.SelectorImagen.value()
        ruta_imagen = self.diccionarDatos[indice]
        self.lbl_imagen.setPixmap(QtGui.QPixmap(ruta_imagen))

    def identificarDino(self):
        indice = self.SelectorImagen.value()
        boton_presionado = self.sender()
        if indice == 1:
            if boton_presionado == self.btn_2:
                self.msj("Correcto")
            else:
                self.msj("Incorrecto")
        elif indice == 2:
            if boton_presionado == self.btn_1:
                self.msj("Correcto")
            else:
                self.msj("Incorrecto")
        elif indice == 3:
            if boton_presionado == self.btn_3:
                self.msj("Correcto")
            else:
                self.msj("Incorrecto")
        elif indice == 4:
            if boton_presionado == self.btn_4:
                self.msj("Correcto")
            else:
                self.msj("Incorrecto")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())