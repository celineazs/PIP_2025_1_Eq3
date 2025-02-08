import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P07_PromedioNumeros.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los Signals
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []
        self.banderaCalif = False
    #Area de los Slots
    def cargar(self):
        if not self.banderaCalif:
        ## EJERCICIO 10 --- TAREA comprobar si el archivo existe
            try:
                archivo = open("../Archivos/calificaciones.csv")
                contenido = archivo.readlines()
                datos = [int(x) for x in contenido]
                ## Ejercicio 11 --- EN LUGAR DE SOBREESCRIBIR CONCATENAR
                print(datos)
                self.calificaciones.extend(datos)
                self.promedio()
            except FileNotFoundError:
                self.msj("No existe el archivo")
        else:
            self.msj("Ya se cargaron las calificaciones")
            ## EJERCICIO 12 --- ASEGURARSE QUE SOLO SE PUEDE CARGAR HASTA ANTES DE
            # AGREGAR LA PRIMERA CALIFICACION ---> ENABLES Y/O/ CODIGO

    def agregar(self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        self.promedio()
        self.banderaCalif = True
        self.btn_cargar.setEnabled(False)

    def promedio(self):
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self):
        archivo = open("../Archivos/calificaciones.csv", "w")
        for c in self.calificaciones:
            archivo.write(str(c) + "\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado con exito")

    def msj (self, txt):
            m = QtWidgets.QMessageBox()
            m.setText(txt)
            m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())