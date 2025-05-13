# Asociador Lineal

# X = Entradas
# Y = Salidas
# W = Y * XPseudoInversa

import numpy as n
import random

archivo = open("Instancias.txt")
contenido = archivo.readlines()

X = contenido[3:3 + int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3 + int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

clase_indices = {0: [], 1: [], 2: []}
for i in range(Y.shape[1]):
    clase = list(Y[:, i]).index(max(Y[:, i]))
    clase_indices[clase].append(i)

entrenamiento = []
validacion = []
for clase in clase_indices:
    random.shuffle(clase_indices[clase])
    entrenamiento += clase_indices[clase][:12]
    validacion += clase_indices[clase][12:15]

Xtrain = X[:, entrenamiento]
Ytrain = Y[:, entrenamiento]

Paso1 = Xtrain.dot(Xtrain.T)
Paso2 = n.linalg.inv(Paso1)
Xpseudo = Xtrain.T.dot(Paso2)

W = Ytrain.dot(Xpseudo)

print("X (entrenamiento):")
print(Xtrain)

print("Y (entrenamiento):")
print(Ytrain)

print("W:")
print(W)

################################################################################
### EVALUACIÓN DE LOS CASOS DE VALIDACIÓN
################################################################################

print("Validación...")

Xval = X[:, validacion]
Yval = Y[:, validacion]

print("X (validación):")
print(Xval)

print("Y (validación):")
print(Yval)

casosCorrectos = 0
Clases = ["BUENO", "REGULAR", "MALO"]

for i in range(Xval.shape[1]):
    print("Prueba del Caso", i + 1)
    casoi = Xval[:, i]
    print("Caso Analizado:")
    print(casoi)

    Ycasoi = W.dot(casoi)
    print("Salidas Generadas:")
    print(Ycasoi)

    print("Salida Real:")
    Yrealcasoi = Yval[:, i]
    print(Yrealcasoi)

    IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
    IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

    if IndexMaxYcasoi == IndexMaxYrealcasoi:
        casosCorrectos += 1

    print("Clase Asignada:", Clases[IndexMaxYcasoi])
    print("Clase Real:", Clases[IndexMaxYrealcasoi])
    print()

print("Total de Casos Analizados:", Xval.shape[1])
print("Total de Casos Correctos:", casosCorrectos)
print("Eficiencia del Asociador Lineal:", casosCorrectos / Xval.shape[1] * 100.0, "%")