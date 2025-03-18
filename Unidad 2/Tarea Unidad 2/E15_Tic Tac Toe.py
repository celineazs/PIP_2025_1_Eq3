import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "E15_Tic Tac Toe.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class TicTacToe(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.x_icon = QtGui.QPixmap(r":/Ejercicios/x.png")
        self.o_icon = QtGui.QPixmap(r":/Ejercicios/Circulo.png")
        self.empty_icon = QtGui.QPixmap(r":/Ejercicios/vacio.png")

        self.buttons = [
            [self.btn_1, self.btn_2, self.btn_3],
            [self.btn_4, self.btn_5, self.btn_6],
            [self.btn_7, self.btn_8, self.btn_9],
        ]

        for row in self.buttons:
            for button in row:
                button.clicked.connect(self.movimiento)

        self.btn_reiniciar.clicked.connect(self.reiniciar)

        self.siguiente = "X"
        self.inicio = [["" for _ in range(3)] for _ in range(3)]

        self.reiniciar()

    def movimiento(self):
        button = self.sender()

        row, col = -1, -1
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j] == button:
                    row, col = i, j
                    break
            if row != -1:
                break

        if self.inicio[row][col] == "":
            self.inicio[row][col] = self.siguiente
            button.setIcon(QtGui.QIcon(self.x_icon if self.siguiente == "X" else self.o_icon))

            if self.revision():
                QMessageBox.information(self, "Juego terminado", f"{self.siguiente} ha ganado!")
                self.final()
                return

            if self.empate():
                QMessageBox.information(self, "Juego terminado", "Es un empate!")
                self.final()
                return

            self.siguiente = "O" if self.siguiente == "X" else "X"

    def revision(self):
        for i in range(3):
            if self.inicio[i][0] == self.inicio[i][1] == self.inicio[i][2] != "":
                return True
            if self.inicio[0][i] == self.inicio[1][i] == self.inicio[2][i] != "":
                return True

        if self.inicio[0][0] == self.inicio[1][1] == self.inicio[2][2] != "":
            return True

        if self.inicio[0][2] == self.inicio[1][1] == self.inicio[2][0] != "":
            return True

        return False

    def empate(self):
        for row in self.inicio:
            if "" in row:
                return False
        return True

    def final(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def reiniciar(self):
        self.siguiente = "X"
        self.inicio = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.setIcon(QtGui.QIcon(self.empty_icon))
                button.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
