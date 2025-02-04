import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "T08_Tabla de Multiplicar.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hs.setMinimum(1)
        self.hs.setMaximum(100)
        self.hs.setSingleStep(5)
        self.hs.setValue(1) #valor inicial
        self.hs.valueChanged.connect(self.cambiaValor)
        self.txt_num.setText("1")

        self.labels = [self.lbl_1, self.lbl_2, self.lbl_3, self.lbl_4, self.lbl_5,
                       self.lbl_6, self.lbl_7, self.lbl_8, self.lbl_9, self.lbl_10]
        self.btn_calcular.clicked.connect(self.calculartabla)


    def cambiaValor(self):
        num=self.hs.value()
        self.txt_num.setText(str(num))


    def calculartabla(self):
        num = self.hs.value()
        for i in range(1,11):
            resultado = num * i
            self.labels[i-1].setText(f"{resultado}")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())