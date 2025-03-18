import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t
qtCreatorFile = "P17_checkbox.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.cb_dormir.clicked.connect(self.dormir)
        self.cb_cine.toggled.connect(self.cine)


    def dormir(self):
        valor = self.cb_dormir.isChecked()
        print("Dormir", valor)

    def cine(self):
        valor = self.cb_cine.isChecked()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())