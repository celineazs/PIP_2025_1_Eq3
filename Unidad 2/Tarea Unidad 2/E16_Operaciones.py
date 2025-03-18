import sys
import random
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E16_Operaciones.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_opcion1.clicked.connect(self.opcion1)
        self.btn_opcion2.clicked.connect(self.opcion2)
        self.btn_opcion3.clicked.connect(self.opcion3)
        self.btn_stop.clicked.connect(self.detener_juego)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.tiempo_restante = 10

        self.aciertos = 0
        self.juego_en_curso = True

        self.nueva_operacion()

    def nueva_operacion(self):
        if not self.juego_en_curso:
            return

        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        operacion = random.choice(["+", "-", "*", "/"])

        if operacion == "+":
            self.correcta = self.num1 + self.num2
            self.lbl_operacion.setText(f"{self.num1} + {self.num2} = ?")
        elif operacion == "-":
            self.correcta = self.num1 - self.num2
            self.lbl_operacion.setText(f"{self.num1} - {self.num2} = ?")
        elif operacion == "*":
            self.correcta = self.num1 * self.num2
            self.lbl_operacion.setText(f"{self.num1} * {self.num2} = ?")
        else:
            if self.num2 == 0 or self.num1 % self.num2 != 0:
                self.num2 = random.randint(1, 10)
                while self.num1 % self.num2 != 0:
                    self.num2 = random.randint(1, 10)
            self.correcta = self.num1 // self.num2
            self.lbl_operacion.setText(f"{self.num1} / {self.num2} = ?")

        opciones = [self.correcta, self.correcta + random.randint(1, 5), self.correcta - random.randint(1, 5)]
        random.shuffle(opciones)

        self.btn_opcion1.setText(str(opciones[0]))
        self.btn_opcion2.setText(str(opciones[1]))
        self.btn_opcion3.setText(str(opciones[2]))
        self.lbl_resultado.setText("")
        self.tiempo_restante = 10
        self.lbl_tiempo.setText(f"Tiempo: {self.tiempo_restante}s")
        self.timer.start(1000)

    def actualizar_tiempo(self):
        if not self.juego_en_curso:
            return

        self.tiempo_restante -= 1
        self.lbl_tiempo.setText(f"Tiempo: {self.tiempo_restante}s")
        if self.tiempo_restante == 0:
            self.tiempo_agotado()

    def verificar_respuesta(self, boton):
        if not self.juego_en_curso:
            return

        self.timer.stop()
        if int(boton.text()) == self.correcta:
            self.aciertos += 1
            self.lbl_resultado.setText(f"¡Correcto! Aciertos: {self.aciertos}")
        else:
            self.lbl_resultado.setText(f"Incorrecto, la respuesta era {self.correcta}")

        QtCore.QTimer.singleShot(2000, self.nueva_operacion)

    def opcion1(self):
        self.verificar_respuesta(self.btn_opcion1)

    def opcion2(self):
        self.verificar_respuesta(self.btn_opcion2)

    def opcion3(self):
        self.verificar_respuesta(self.btn_opcion3)

    def tiempo_agotado(self):
        self.timer.stop()
        self.lbl_resultado.setText(f"¡Tiempo agotado! La respuesta era {self.correcta}")
        QtCore.QTimer.singleShot(2000, self.nueva_operacion)

    def detener_juego(self, respuesta=None):
        self.juego_en_curso = False
        self.timer.stop()
        QMessageBox.information(self, "Juego Detenido", f"Juego detenido. Aciertos totales: {self.aciertos}",QMessageBox.Ok)
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
