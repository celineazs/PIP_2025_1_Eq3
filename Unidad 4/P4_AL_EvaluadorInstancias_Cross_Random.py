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

# Determinar la clase de cada instancia
clase_indices = {0: [], 1: [], 2: []}
for i in range(Y.shape[1]):
    clase = list(Y[:, i]).index(max(Y[:, i]))
    clase_indices[clase].append(i)

# Elegir número de segmentos aleatoriamente entre 2 y 10
ns = random.randint(2, 10)
print(f"\nSe usarán {ns} folds para validación cruzada.")

# Crear segmentos
segmentos = [[] for _ in range(ns)]
for clase in clase_indices:
    indices = clase_indices[clase]
    random.shuffle(indices)
    tamaño_segmento = len(indices) // ns
    for i in range(ns):
        inicio = i * tamaño_segmento
        fin = (i + 1) * tamaño_segmento if i != ns - 1 else len(indices)
        segmentos[i] += indices[inicio:fin]

eficiencias = []
Clases = ["BUENO", "REGULAR", "MALO"]

# Validación cruzada
for fold in range(ns):
    print(f"\n========= VALIDACIÓN {fold + 1} =========")

    validacion = segmentos[fold]
    entrenamiento = []
    for i in range(ns):
        if i != fold:
            entrenamiento += segmentos[i]

    print("Índices de entrenamiento:", entrenamiento)
    print("Índices de validación:", validacion)

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

    # Evaluación
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

# Resultados finales
print("\n========= RESULTADOS FINALES =========")
for i, e in enumerate(eficiencias):
    print(f"Fold {i + 1}: {e:.2f}%")
print(f"Promedio de eficiencia: {sum(eficiencias) / len(eficiencias):.2f}%")
