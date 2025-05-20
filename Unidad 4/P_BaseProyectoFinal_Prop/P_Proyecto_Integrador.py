import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import serial as tarjeta

import Dialogo_ConexionArduino
from P_Plantilla_Principal import Ui_MainWindow



class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals

        # Ocultar elementos desde el inicio
        self.txt_pir.hide()
        self.btn_ocultar1.hide()

        self.txt_puerta.hide()
        self.btn_ocultar2.hide()

        self.txt_ldr.hide()
        self.btn_ocultar3.hide()

        # Conectar botones mostrar
        self.btn_mostrar_1.clicked.connect(self.mostrar_pir)
        self.btn_mostrar_2.clicked.connect(self.mostrar_puerta)
        self.btn_mostrar_3.clicked.connect(self.mostrar_ldr)

        # Conectar botones ocultar
        self.btn_ocultar1.clicked.connect(self.ocultar_pir)
        self.btn_ocultar2.clicked.connect(self.ocultar_puerta)
        self.btn_ocultar3.clicked.connect(self.ocultar_ldr)

        self.arduino = None

        self.btn_iniciar.clicked.connect(self.iniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturas)

        self.bandera = 0
        self.datos = []

        #self.btn_led1.clicked.connect(self.control)
        #self.btn_led2.clicked.connect(self.control)
        #self.btn_led3.clicked.connect(self.control)

    # Área de los Slots

    def mostrar_pir(self):
        self.txt_pir.show()
        self.btn_ocultar1.show()
        self.btn_mostrar_1.hide()

    def ocultar_pir(self):
        self.txt_pir.hide()
        self.btn_ocultar1.hide()
        self.btn_mostrar_1.show()

    def mostrar_puerta(self):
        self.txt_puerta.show()
        self.btn_ocultar2.show()
        self.btn_mostrar_2.hide()

    def ocultar_puerta(self):
        self.txt_puerta.hide()
        self.btn_ocultar2.hide()
        self.btn_mostrar_2.show()

    def mostrar_ldr(self):
        self.txt_ldr.show()
        self.btn_ocultar3.show()
        self.btn_mostrar_3.hide()

    def ocultar_ldr(self):
        self.txt_ldr.hide()
        self.btn_ocultar3.hide()
        self.btn_mostrar_3.show()

    def iniciar(self):
        if self.arduino is None:
            self.dialogo = Dialogo_ConexionArduino.MyDialog(self)
            self.dialogo.setModal(True)
            self.dialogo.show()
            self.segundoPlano.start(100)
            self.txt_estado.setText("CONECTADO")
        else:
            if self.arduino.isOpen():
                self.arduino.close()
                self.txt_estado.setText("DESCONECTADO")
                self.segundoPlano.stop()
                self.arduino = None

    def control(self):
        obj = self.sender()
        texto = obj.text()
        led = obj.objectName()[-1]
        if self.arduino.isOpen():
            if texto == "PRENDER":
                obj.setText("APAGAR")
                c = led + "1"
                self.arduino.write(c.encode())
            else:
                obj.setText("PRENDER")
                c = led + "0"
                self.arduino.write(c.encode())

    def lecturas(self):
        if self.arduino and self.arduino.isOpen():
            if self.arduino.inWaiting():
                cadena = self.arduino.readline().decode().strip()
                if cadena != "":
                    print("Cadena recibida:", cadena)

                    if "Movimiento" in cadena or "mov" in cadena:
                        self.txt_pir.appendPlainText(cadena)
                    elif "Puerta" in cadena or "puerta" in cadena:
                        self.txt_puerta.appendPlainText(cadena)
                    elif "Luz" in cadena or "Luces" in cadena or "Dia" in cadena or "Noche" in cadena:
                        self.txt_ldr.appendPlainText(cadena)
                    else:
                        self.lista_datos.addItem(cadena)
                        self.lista_datos.setCurrentRow(self.lista_datos.count() - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())