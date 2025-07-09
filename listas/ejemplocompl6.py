cantidad_elementos = int(input("tamanio del vector: "))
vector_numeros = []
for i in range (cantidad_elementos):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    vector_numeros.append(numero)
print(vector_numeros)
for pasada in range(cantidad_elementos):
    for indice in range(cantidad_elementos - 1):
        if vector_numeros[indice] < vector_numeros[indice + 1]:
            auxiliar = vector_numeros[indice]
            vector_numeros[indice] = vector_numeros[indice + 1]
            vector_numeros[indice + 1] = auxiliar
print("\nVector ordenado de mayor a menor:", vector_numeros)    