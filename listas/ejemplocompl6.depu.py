# -*- coding: utf-8 -*-
print("-------------------------------------------------------")
print("Complemento6: ORDENAR DESCENDENTEMENTE EL VECTOR - EXPLICADO")
print("-------------------------------------------------------")

# Paso 1: Inicializar el vector vacío
vector_numeros = []

# Paso 2: Leer la cantidad de elementos
cantidad_elementos = int(input("Ingrese la cantidad de elementos del vector: "))

# Paso 3: Cargar los números dentro del vector
print("Ingrese los valores del vector:")
for posicion in range(cantidad_elementos):
    numero = int(input(f"Elemento {posicion + 1}: "))
    vector_numeros.append(numero)

# Mostrar el vector original
print("\nVector original:", vector_numeros)

# Paso 4: Ordenar el vector manualmente de mayor a menor (Burbuja Descendente)
for pasada in range(cantidad_elementos):
    print(f"\n🔄 Pasada {pasada + 1}:")

    for indice in range(cantidad_elementos - 1):
        num_actual = vector_numeros[indice]
        num_siguiente = vector_numeros[indice + 1]

        print(f"Comparando posición {indice} ({num_actual}) con posición {indice + 1} ({num_siguiente})")

        if num_actual < num_siguiente:
            # Mensaje explicativo del intercambio
            print(f"➡ Intercambiando {num_actual} y {num_siguiente} para colocar el mayor primero")

            # Intercambio manual utilizando variable auxiliar
            auxiliar = vector_numeros[indice]
            vector_numeros[indice] = vector_numeros[indice + 1]
            vector_numeros[indice + 1] = auxiliar

            print("➡ Vector actualizado:", vector_numeros)
        else:
            print("✔ No se intercambia")

# Paso 5: Mostrar el resultado final
print("\n✅ Vector final ordenado de mayor a menor:", vector_numeros)

