import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E11_Reloj_Alarma.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class RelojAlarma(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hora = 12
        self.minuto = 0
        self.segundo = 0
        self.alarma = None
        self.alarma_sonando = False

        self.btn_ajustar_hora.clicked.connect(self.ajustar_hora)
        self.btn_ajustar_alarma.clicked.connect(self.ajustar_alarma)
        self.btn_stop_alarm.clicked.connect(self.detener_alarma)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_hora)
        self.timer.start(1000)
        self.actualizar_hora()

    def actualizar_hora(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto >= 60:
            self.minuto = 0
            self.hora = (self.hora + 1) % 24

        texto = f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"
        self.lbl_time.setText(texto)

        if self.alarma and not self.alarma_sonando:
            if (self.hora, self.minuto, self.segundo) == self.alarma:
                self.alarma_sonando = True
                QMessageBox.information(self, "Alarma", "¡Es hora de la alarma!")

    def ajustar_hora(self):
        hora = self.edit_hora.time()
        self.hora = hora.hour()
        self.minuto = hora.minute()
        self.segundo = hora.second()
        self.actualizar_hora()

    def ajustar_alarma(self):
        hora = self.edit_alarma.time()
        self.alarma = (hora.hour(), hora.minute(), hora.second())
        self.alarma_sonando = False
        QMessageBox.information(self, "Alarma Configurada",
            f"La alarma sonará a las {hora.toString('HH:mm:ss')}")

    def detener_alarma(self):
        if self.alarma_sonando:
            self.alarma_sonando = False
            QMessageBox.information(self, "Alarma", "La alarma ha sido detenida.")
        else:
            QMessageBox.information(self,"No hay una alarma sonando.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RelojAlarma()
    window.show()
    sys.exit(app.exec_())
