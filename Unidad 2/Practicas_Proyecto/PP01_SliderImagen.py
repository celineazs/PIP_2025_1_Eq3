import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "PP01_Slider.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los signals
        self.patron = [1,2,3,4,5,6,7,8,9,10]
        self.imagenactual = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.cambiaValor)
        self.timer.start(1000)

        self.diccionarDatos = {
            1: ":/Ejercicios/spiderman.jpg",
            2: ":/Ejercicios/superman.jpg",
            3: ":/Ejercicios/flash.jpg",
            4: ":/Ejercicios/batman.jpg",
            5: ":/Ejercicios/capitan.jpg",
            6: ":/Ejercicios/koya.jpg",
            7: ":/Ejercicios/cooky.jpg",
            8: ":/Ejercicios/tata.jpg",
            9: ":/Ejercicios/rj.jpg",
            10: ":/Ejercicios/chimmy.jpg"
        }

        self.cambiaValor()


    def cambiaValor(self):
        if self.imagenactual < len(self.patron):
            ruta_imagen = self.patron[self.imagenactual]
            self.lbl_imagen.setPixmap(QtGui.QPixmap(self.diccionarDatos[ruta_imagen]))
            self.imagenactual += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())