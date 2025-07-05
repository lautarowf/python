print("-------------------------------------------------------")
print("Complemento2: INVERTIR VECTOR DE CARACTERES.")
print("-------------------------------------------------------")

# Entrada: Pedir la cantidad de caracteres (tamaño del vector)
tamanio_vector = int(input("Ingrese dimensión del vector: "))

# Inicialización del vector con el tamaño indicado
vector_caracteres = tamanio_vector * ['']

# Cargar el vector con caracteres ingresados por el usuario
for posicion in range(tamanio_vector):
    vector_caracteres[posicion] = input(f"Ingrese el carácter {posicion + 1}: ")

# Proceso: Invertir el vector sin usar vector auxiliar
posicion_final = tamanio_vector  # Marca el índice de los elementos finales

for posicion_inicial in range(tamanio_vector // 2):
    # Guardar el carácter en una variable temporal
    temporal = vector_caracteres[posicion_inicial]

    # Intercambiar los caracteres de los extremos
    vector_caracteres[posicion_inicial] = vector_caracteres[posicion_final - 1]
    vector_caracteres[posicion_final - 1] = temporal

    # Reducir la posición final
    posicion_final = posicion_final - 1

# Salida: Mostrar el vector invertido
print("Vector invertido:")
for caracter in vector_caracteres:
    print(caracter)
