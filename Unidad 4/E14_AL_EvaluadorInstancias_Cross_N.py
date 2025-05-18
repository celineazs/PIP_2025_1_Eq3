# Asociador Lineal con Validación Cruzada de n segmentos
import numpy as n
import random

# === Lectura de archivo ===
archivo = open("Instancias2.txt")
contenido = archivo.readlines()

X = contenido[3:3 + int(contenido[1])]
X = [i.strip().split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3 + int(contenido[1]):]
Y = [i.strip().split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = n.array(X)
Y = n.array(Y)

# === Preparar índices por clase ===
clase_indices = {0: [], 1: [], 2: []}
for i in range(Y.shape[1]):
    clase = list(Y[:, i]).index(max(Y[:, i]))
    clase_indices[clase].append(i)

# === Mezclar e insertar en segmentos ===
ns = 9  # Número de folds deseado
segmentos = [[] for _ in range(ns)]
for clase in clase_indices:
    indices = clase_indices[clase]
    random.shuffle(indices)
    tamaño_segmento = len(indices) // ns
    for i in range(ns):
        inicio = i * tamaño_segmento
        fin = (i + 1) * tamaño_segmento if i != ns - 1 else len(indices)
        segmentos[i] += indices[inicio:fin]

# === Validación Cruzada ===
eficiencias = []
Clases = ["BUENO", "REGULAR", "MALO"]

for fold in range(ns):
    print(f"\n========= VALIDACIÓN {fold + 1} =========")

    validacion = segmentos[fold]
    entrenamiento = []
    for i in range(ns):
        if i != fold:
            entrenamiento += segmentos[i]

    # Mostrar valores reales de las instancias
    print("\nX (entrenamiento):")
    print(n.array2string(X[:, entrenamiento], separator=", "))
    print("Y (entrenamiento):")
    print(n.array2string(Y[:, entrenamiento], separator=", "))

    print("\nX (validación):")
    print(n.array2string(X[:, validacion], separator=", "))
    print("Y (validación):")
    print(n.array2string(Y[:, validacion], separator=", "))

    # === Asociador Lineal ===
    Xtrain = X[:, entrenamiento]
    Ytrain = Y[:, entrenamiento]
    Xval = X[:, validacion]
    Yval = Y[:, validacion]

    Paso1 = Xtrain.dot(Xtrain.T)
    Paso2 = n.linalg.inv(Paso1)
    Xpseudo = Xtrain.T.dot(Paso2)
    W = Ytrain.dot(Xpseudo)

    print("\nW:")
    print(n.array2string(W, separator=", "))

    print("\nValidación...")
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

# === Resultados Finales ===
print("\n========= RESULTADOS FINALES =========")
for i, e in enumerate(eficiencias):
    print(f"Eficiencia segmento {i+1}: {e:.2f}%")
print(f"Promedio de eficiencia: {sum(eficiencias) / len(eficiencias):.2f}%")
