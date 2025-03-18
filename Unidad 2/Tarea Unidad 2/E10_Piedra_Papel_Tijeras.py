import sys
import os
import resource_rc
import random
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E10_Piedra_Papel_Tijeras.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class PiedraPapelTijeras(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.piedra_icon = QtGui.QPixmap(r":/Ejercicios/piedra.png")
        self.papel_icon = QtGui.QPixmap(r":/Ejercicios/papel.png")
        self.tijeras_icon = QtGui.QPixmap(r":/Ejercicios/tijeras.png")
        self.empty_icon = QtGui.QPixmap(r":/Ejercicios/vacio.png")

        self.btn_piedra.clicked.connect(self.jugar_piedra)
        self.btn_papel.clicked.connect(self.jugar_papel)
        self.btn_tijeras.clicked.connect(self.jugar_tijeras)
        self.btn_reiniciar.clicked.connect(self.reiniciar)

        self.opciones = ["Piedra", "Papel", "Tijeras"]
        self.reiniciar()

    def jugar(self, eleccion_jugador):
        eleccion_pc = random.choice(self.opciones)

        self.lbl_jugador.setPixmap(self.get_icon(eleccion_jugador))
        self.lbl_pc.setPixmap(self.get_icon(eleccion_pc))

        resultado = self.determinar_ganador(eleccion_jugador, eleccion_pc)
        QMessageBox.information(self, "Resultado", resultado)

    def jugar_piedra(self):
        self.jugar("Piedra")

    def jugar_papel(self):
        self.jugar("Papel")

    def jugar_tijeras(self):
        self.jugar("Tijeras")

    def determinar_ganador(self, jugador, pc):
        if jugador == pc:
            return "Empate!"
        elif (jugador == "Piedra" and pc == "Tijeras") or \
             (jugador == "Papel" and pc == "Piedra") or \
             (jugador == "Tijeras" and pc == "Papel"):
            return "¡Ganaste!"
        else:
            return "Perdiste!"

    def get_icon(self, opcion):
        if opcion == "Piedra":
            return self.piedra_icon
        elif opcion == "Papel":
            return self.papel_icon
        elif opcion == "Tijeras":
            return self.tijeras_icon
        return self.empty_icon

    def reiniciar(self):
        self.lbl_jugador.setPixmap(self.empty_icon)
        self.lbl_pc.setPixmap(self.empty_icon)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PiedraPapelTijeras()
    window.show()
    sys.exit(app.exec_())
