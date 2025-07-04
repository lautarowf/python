vector_original = []
cantidad_de_elementos = int(input("Ingrese la cantidad de elementos: "))
if 1 <= cantidad_de_elementos <= 200:
    for i in range(1, cantidad_de_elementos+1):
        numero_ingresado = int(input(f"Ingrese el numero {i}: "))
        vector_original.append(numero_ingresado)
    vector_sin_repeticiones = []
    for numero in vector_original:
        if numero not in vector_sin_repeticiones:
            vector_sin_repeticiones.append(numero)
    vector_sin_repeticiones.sort()
    print(vector_sin_repeticiones)
else:
    print("error")