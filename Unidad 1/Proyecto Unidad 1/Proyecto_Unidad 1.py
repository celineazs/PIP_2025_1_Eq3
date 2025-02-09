import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Proyecto_Unidad 1.ui"
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
        self.valores = []
        self.bandera = False

    #Area de los Slots
    def cargar(self):
        if not self.bandera:
            try:
                archivo = open("../Archivos/valores.csv")
                contenido = archivo.readlines()
                datos = [int(x) for x in contenido]
                print(datos)
                self.valores.extend(datos)
                self.txt_valores.setText(str(self.valores))

                with open("../Archivos/analisis_estadistico.csv") as archivo_estadistico:
                    lineas = archivo_estadistico.readlines()
                    for linea in lineas:
                        medida, valor = linea.strip().split(",")
                        if medida == "Promedio":
                            self.txt_media.setText(valor)
                        elif medida == "Mediana":
                            self.txt_mediana.setText(valor)
                        elif medida == "Moda":
                            self.txt_moda.setText(valor)
                        elif medida == "Varianza":
                            self.txt_varianza.setText(valor)
                        elif medida == "Desviación Estándar":
                            self.txt_desviacion.setText(valor)
                        elif medida == "Valor Mínimo":
                            self.txt_valorMe.setText(valor)
                        elif medida == "Valor Máximo":
                            self.txt_valorMa.setText(valor)

            except FileNotFoundError:
                self.msj("No existe el archivo")
        else:
            self.msj("Ya se cargaron los valores")


    def agregar(self):
        valor = int(self.txt_ingresar.text())
        self.valores.append(valor)
        self.Calculos()
        self.txt_valores.setText(str(self.valores))
        self.bandera = True
        self.btn_cargar.setEnabled(False)
        self.txt_ingresar.setText("")

    def Calculos(self):
        self.valorMenoryMayor()
        self.TendenciaCentral()
        self.VarianzayDesviacion()

    def valorMenoryMayor(self):
        menor = min(self.valores)
        mayor = max(self.valores)
        self.txt_valorMe.setText(str(menor))
        self.txt_valorMa.setText(str(mayor))

    def TendenciaCentral(self):
        #moda
        moda = max(set(self.valores), key = self.valores.count)
        self.txt_moda.setText(str(moda))

        #promedio
        prom = sum(self.valores) / len(self.valores)
        self.txt_media.setText(f"{prom:.2f}")

        #mediana
        valores_ordenados = sorted(self.valores)
        n = len(valores_ordenados)
        mitad = n // 2
        if n % 2 == 0:
            mediana = (valores_ordenados[mitad - 1] + valores_ordenados[mitad]) / 2
        else:
            mediana = valores_ordenados[mitad]
        self.txt_mediana.setText(str(mediana))

    def VarianzayDesviacion(self):
        prom = sum(self.valores) / len(self.valores)
        varianza = sum((xi - prom) ** 2 for xi in self.valores) / len(self.valores)
        desviacion = varianza ** 0.5
        self.txt_varianza.setText(f"{varianza:.2f}")
        self.txt_desviacion.setText(f"{desviacion:.2f}")

    def guardar(self):
        with open("../Archivos/valores.csv", "w") as archivo:
            for c in self.valores:
                archivo.write(f"{c}\n")

        with open("../Archivos/analisis_estadistico.csv", "w") as archivo_estadistico:
            archivo_estadistico.write(f"Promedio,{self.txt_media.text()}\n")
            archivo_estadistico.write(f"Mediana,{self.txt_mediana.text()}\n")
            archivo_estadistico.write(f"Moda,{self.txt_moda.text()}\n")
            archivo_estadistico.write(f"Varianza,{self.txt_varianza.text()}\n")
            archivo_estadistico.write(f"Desviación Estándar,{self.txt_desviacion.text()}\n")
            archivo_estadistico.write(f"Valor Mínimo,{self.txt_valorMe.text()}\n")
            archivo_estadistico.write(f"Valor Máximo,{self.txt_valorMa.text()}\n")

        self.msj("Archivos guardados con éxito")

    def msj (self, txt):
            m = QtWidgets.QMessageBox()
            m.setText(txt)
            m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window= MyApp()
    window.show()
    sys.exit(app.exec_())