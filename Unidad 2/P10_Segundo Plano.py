import sys
from PyQt5 import uic, QtWidgets, QtCore
import time as t
qtCreatorFile = "P10_SegundoPlanoTimer.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_temporizar.clicked.connect(self.temporizar2doPlano())
        self.SegundoPlano = QtCore.QTimer()
        self.SegundoPlano.timeout.connect(self.controlSegundoPlano)
        self.ValorN = -1

    def controlSegundoPlano(self):
        self.txt_temporizador.setText(str(self.ValorN))
        self.ValorN -= 1
        if self.ValorN == -1:
            self.SegundoPlano.stop()

    def temporizar2doPlano(self):
        self.ValorN = int(self.txt_temporizador.text())
        self.SegundoPlano.start(500)

    def temporizar(self):
        valor = int(self.txt_temporizador.text())
        for i in range(valor, 0, -1):
            self.txt_temporizador.setText(str(i))
            print(i)
            t.sleep(0.5)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())