import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t
qtCreatorFile = "P18_Checkbox_V2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.cb_dormir.clicked.connect(self.control)
        self.cb_cine.toggled.connect(self.control)



    def control(self):
        obj= self.sender()
        valor = obj.isChecked()
        print("Objeto", obj.text(),":",valor)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())