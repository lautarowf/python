# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Matriz1: SUMA DE MATRICES")
print("-------------------------------------------------------")

# Inicialización de las tres matrices vacías
matriz_A = []
matriz_B = []
matriz_C = []

# Entradas: Dimensiones de las matrices
print("Ingrese la dimensión de las matrices (máximo 100)")
cantidad_filas = int(input("Número de filas: "))
cantidad_columnas = int(input("Número de columnas: "))

# Verificación opcional (no estaba en el original)
if cantidad_filas <= 100 and cantidad_columnas <= 100:
    
    # Carga de datos y suma de matrices
    for fila in range(cantidad_filas):
        # Agregar listas vacías por cada fila
        matriz_A.append([])
        matriz_B.append([])
        matriz_C.append([])
        
        for columna in range(cantidad_columnas):
            # Pedir valores para cada celda
            valor_A = int(input(f"Ingrese el valor de A[{fila+1}][{columna+1}]: "))
            valor_B = int(input(f"Ingrese el valor de B[{fila+1}][{columna+1}]: "))
            
            # Agregar valores a las matrices A y B
            matriz_A[fila].append(valor_A)
            matriz_B[fila].append(valor_B)
            
            # Calcular la suma y agregar a la matriz C
            suma = valor_A + valor_B
            matriz_C[fila].append(suma)
    
    # Salida: Mostrar las matrices
    print("\nSALIDA:")
    print("-------------------------------------------------------")
    print("Matriz A:")
    for fila in matriz_A:
        print(fila)
    
    print("\nMatriz B:")
    for fila in matriz_B:
        print(fila)
    
    print("\nMatriz C (Suma):")
    for fila in matriz_C:
        print(fila)

else:
    print("Error: Las dimensiones no pueden superar 100 filas o columnas.")
