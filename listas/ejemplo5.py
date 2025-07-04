print("Matriz2: VERIFICAR SI LA MATRIZ ES SIMÉTRICA.")
print("-------------------------------------------------------")

# Inicialización
matriz = []

# Entrada: Leer dimensión
print("Ingrese la dimensión de la matriz (cuadrada):")
dimension = int(input())

# Verificar que la dimensión sea válida
if 1 <= dimension <= 100:

    # Cargar la matriz
    for fila in range(dimension):
        matriz.append([])  # Agregar una fila vacía
        for columna in range(dimension):
            valor = int(input(f"Ingrese el valor en la posición A[{fila}][{columna}]: "))
            matriz[fila].append(valor)

    # Verificación de simetría
    es_simetrica = True
    fila = 0

    while fila < dimension and es_simetrica:
        columna = 0
        while columna < fila and es_simetrica:  # Solo se revisa la mitad inferior
            if matriz[fila][columna] != matriz[columna][fila]:
                es_simetrica = False
            columna += 1
        fila += 1

    # Salida
    if es_simetrica:
        print("La matriz SÍ es simétrica.")
    else:
        print("La matriz NO es simétrica.")
else:
    print("Error: La dimensión debe estar entre 1 y 100.")