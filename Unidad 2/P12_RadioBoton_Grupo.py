import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t
qtCreatorFile = "P12_RadioBoton_grupo.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.rb_perro.clicked.connect(self.perro)
        self.rb_gato.clicked.connect(self.gato)
        self.rb_hamster.clicked.connect(self.Hamster)

        self.rb_negro.toggled.connect(self.negro)
        self.rb_rojo.toggled.connect(self.rojo)
        self.rb_azul.toggled.connect(self.azul)

    def perro(self):
        print("Perro")

    def gato(self):
        print("Gato")

    def Hamster(self):
        print("Hamster")

    def negro(self):
       v = self.rb_negro.isChecked()
       print("negro", v)

    def rojo(self):
        v = self.rb_rojo.isChecked()
        print("rojo", v)

    def azul(self):
        v = self.rb_azul.isChecked()
        print("azul", v)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())