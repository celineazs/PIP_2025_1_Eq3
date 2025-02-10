import sys
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QTimer

qtCreatorFile = "E13_Contador_de_clicks.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.clics = 0
        self.tiempo= 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.btn_iniciar.clicked.connect(self.iniciar_temporizador)
        self.btn_click.clicked.connect(self.incrementar_contador)

    def iniciar_temporizador(self):
        try:
            self.tiempo = int(self.txt_tiempo.text())
            self.clics = 0
            self.txt_contador.setText("0")
            self.timer.start(1000)
            self.btn_click.setEnabled(True)
        except ValueError:
            self.txt_tiempo.setText("")

    def actualizar_tiempo(self):
        if self.tiempo > 0:
            self.tiempo -= 1
            self.txt_tiempo.setText(str(self.tiempo))
        else:
            self.timer.stop()
            self.btn_click.setEnabled(False)
            self.msj()

    def incrementar_contador(self):
        if self.timer.isActive():
            self.clics += 1
            self.txt_contador.setText(str(self.clics))

    def msj(self):
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Contador Finalizado")
        m.setText(f"Número total de clics: {self.clics}")
        m.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())