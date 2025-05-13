import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

import Plantilla_Grafica as gui
import matplotlib.pyplot as plt

class MyApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        gui.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)
        self.btn_graficar.clicked.connect(self.graficar)

        self.x = [i for i in range(50)]
        self.y = []
    def lecturas(self):
        self.segundoPlano.timeout(100)

    def graficar(self):

        import random as rnd
        while len(self.y) < len(self.x):
            t = rnd.randint(0,1023)
            self.y.append(t)
        self.ax.plot(self.x,self.y)
        self.canvas.draw()
        plt.cla()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
