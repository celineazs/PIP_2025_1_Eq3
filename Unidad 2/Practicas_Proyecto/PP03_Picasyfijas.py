import sys
from random import random, randint

from PyQt5 import uic, QtWidgets
qtCreatorFile = "PP03_Picasyfijas.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.contador = 0
        self.numeroAleatorio = ""
        self.btn_nuevojuego.clicked.connect(self.nuevojuego)
        self.btn_comprobar.clicked.connect(self.comprobar)
        self.btn_borrar.clicked.connect(self.borrar)
        # Area de los Signals

    # Area de los Slots
    def nuevojuego(self):
        self.numeroAleatorio = str(randint(100, 999))
        self.txt_resultado.clear()
        self.txt_intento.clear()
        self.contador = 0
        self.msj("Iniciando nuevo juego")

    def comprobar(self):
        self.valor1 = self.txt_numuno.text()
        self.valor2 = self.txt_numdos.text()
        self.valor3 = self.txt_numtres.text()
        intento = self.valor1 + self.valor2 + self.valor3
        if len(intento) != 3:
            self.msj("Favor de ingresar un numero de 3 digitos")
            return
        picas, fijas = self.calculo_picas_fijas(intento)
        self.contador += 1
        self.txt_resultado.setText(f'Intento {self.contador}: {intento} - Picas: {picas}, Fijas: {fijas}')
        self.txt_intento.setText(f"{self.contador}")
        self.txt_numuno.clear()
        self.txt_numdos.clear()
        self.txt_numtres.clear()
        if fijas == 3:
            self.msj(f"Has adivinado el numero en {self.contador} intentos")
            self.nuevojuego()


    def borrar(self):
        self.txt_resultado.clear()
        self.txt_intento.clear()
        self.msj("Borrando intentos")

    def calculo_picas_fijas(self, intento):
        picas = 0
        fijas = 0
        for i in range(3):
            if intento[i] == self.numeroAleatorio[i]:
                fijas += 1
            elif intento[i] in self.numeroAleatorio:
                picas += 1
        return picas, fijas

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())