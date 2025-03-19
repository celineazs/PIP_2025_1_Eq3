import sys
import random
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QTimer

qtCreatorFile = "Proyecto_Memorama.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Lista de imágenes
        self.images = [":Ejercicios/chimmy.jpg", ":Ejercicios/cooky.jpg", ":Ejercicios/spiderman.jpg",
                       ":Ejercicios/superman.jpg", ":Ejercicios/batman.jpg", ":Ejercicios/flash.jpg"] * 2  # Pares

        random.shuffle(self.images)  # Mezclar imágenes

        # Lista de botones
        self.buttons = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6,
                        self.btn_7, self.btn_8, self.btn_9, self.btn_10, self.btn_11, self.btn_12]

        # Asignar imágenes ocultas a cada botón
        self.assigned_images = {}
        for i, button in enumerate(self.buttons):
            self.assigned_images[button] = self.images[i]
            button.setIcon(QtGui.QIcon(r":Ejercicios/vacio.png"))  # Imagen de reverso
            button.setIconSize(button.size())
            button.clicked.connect(lambda checked, btn=button: self.reveal_card(btn))

        self.first_card = None
        self.second_card = None

        self.btn_reiniciar.clicked.connect(self.reset_game)

    def reveal_card(self, button):
        if button in (self.first_card, self.second_card):
            return

        button.setIcon(QtGui.QIcon(self.assigned_images[button]))
        button.setIconSize(button.size())

        if self.first_card is None:
            self.first_card = button
        elif self.second_card is None:
            self.second_card = button
            QtWidgets.QApplication.processEvents()
            self.check_match()

    def check_match(self):
        if self.assigned_images[self.first_card] == self.assigned_images[self.second_card]:
            self.first_card.setEnabled(False)
            self.second_card.setEnabled(False)
            self.first_card = None
            self.second_card = None
        else:
            QTimer.singleShot(500, self.hide_cards)

    def hide_cards(self):
        self.first_card.setIcon(QtGui.QIcon(r":Ejercicios/vacio.png"))
        self.second_card.setIcon(QtGui.QIcon(r":Ejercicios/vacio.png"))
        self.first_card = None
        self.second_card = None

    def reset_game(self):
        random.shuffle(self.images)
        for i, button in enumerate(self.buttons):
            self.assigned_images[button] = self.images[i]
            button.setIcon(QtGui.QIcon(r":Ejercicios/vacio.png"))
            button.setIconSize(button.size())
            button.setEnabled(True)

        self.first_card = None
        self.second_card = None

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
