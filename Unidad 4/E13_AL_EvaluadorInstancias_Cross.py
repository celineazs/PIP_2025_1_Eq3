# Asociador Lineal con Validación Cruzada (5 Folds)
import numpy as n
import random

# Leer archivo
archivo = open("Instancias2.txt")
contenido = archivo.readlines()

# Procesar X
X = contenido[3:3 + int(contenido[1])]
X = [i.strip().split("\t") for i in X]
X = [list(map(int, i)) for i in X]

# Procesar Y
Y = contenido[3 + int(contenido[1]):]
Y = [i.strip().split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

# Separar índices por clase
clase_indices = {0: [], 1: [], 2: []}
for i in range(Y.shape[1]):
    clase = list(Y[:, i]).index(max(Y[:, i]))
    clase_indices[clase].append(i)

# Mezclar los índices por clase
for clase in clase_indices:
    random.shuffle(clase_indices[clase])

# Dividir en 5 segmentos balanceados por clase
segmentos = [[] for _ in range(5)]
for clase in clase_indices:
    indices = clase_indices[clase]
    for i in range(5):
        segmentos[i] += indices[i*3:(i+1)*3]  # 3 instancias por clase por fold

eficiencias = []
Clases = ["BUENO", "REGULAR", "MALO"]

# Validación cruzada
for fold in range(5):
    print(f"\n========= VALIDACIÓN {fold + 1} =========")

    # Validación: fold actual
    validacion = segmentos[fold]

    # Entrenamiento: todos los demás
    entrenamiento = []
    for i in range(5):
        if i != fold:
            entrenamiento += segmentos[i]

    print("Índices de entrenamiento:", entrenamiento)
    print("Índices de validación:", validacion)

    # Crear conjuntos de entrenamiento y validación
    Xtrain = X[:, entrenamiento]
    Ytrain = Y[:, entrenamiento]
    Xval = X[:, validacion]
    Yval = Y[:, validacion]

    print("\nX (entrenamiento):")
    print(n.array2string(Xtrain, separator=", "))
    print("\nY (entrenamiento):")
    print(n.array2string(Ytrain, separator=", "))

    # Calcular W
    Paso1 = Xtrain.dot(Xtrain.T)
    Paso2 = n.linalg.inv(Paso1)
    Xpseudo = Xtrain.T.dot(Paso2)
    W = Ytrain.dot(Xpseudo)

    print("\nW:")
    print(n.array2string(W, separator=", "))

    # Evaluar
    print("Validación...")
    print("\nX (validación):")
    print(n.array2string(Xval, separator=", "))
    print("\nY (validación):")
    print(n.array2string(Yval, separator=", "))

    casosCorrectos = 0
    for i in range(Xval.shape[1]):
        casoi = Xval[:, i]
        Ycasoi = W.dot(casoi)
        Yrealcasoi = Yval[:, i]

        IndexMaxYcasoi = list(Ycasoi).index(max(Ycasoi))
        IndexMaxYrealcasoi = list(Yrealcasoi).index(max(Yrealcasoi))

        if IndexMaxYcasoi == IndexMaxYrealcasoi:
            casosCorrectos += 1

        print(f"Caso {i + 1}: Asignada = {Clases[IndexMaxYcasoi]}, Real = {Clases[IndexMaxYrealcasoi]}")

    eficiencia = casosCorrectos / Xval.shape[1] * 100.0
    eficiencias.append(eficiencia)
    print(f"Eficiencia en validación {fold + 1}: {eficiencia:.2f}%")

# Resultado final
print("\n========= RESULTADOS FINALES =========")
for i, e in enumerate(eficiencias):
    print(f"Fold {i+1}: {e:.2f}%")
print(f"Promedio de eficiencia: {sum(eficiencias) / len(eficiencias):.2f}%")
