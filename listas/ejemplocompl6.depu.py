# -*- coding: utf-8 -*-
print("-------------------------------------------------------")
print("Complemento6: ORDENAR DESCENDENTEMENTE EL VECTOR - EXPLICADO")
print("-------------------------------------------------------")

# Paso 1: Inicializar vector
vector_numeros = []

# Paso 2: Leer cantidad de elementos
cantidad_elementos = int(input("Ingrese la cantidad de elementos del vector: "))

# Paso 3: Cargar los números
print("Ingrese los valores del vector:")
for posicion in range(cantidad_elementos):
    numero = int(input(f"Elemento {posicion + 1}: "))
    vector_numeros.append(numero)

print("\nVector original:", vector_numeros)

# Paso 4: Ordenar manualmente (Burbuja Descendente) con EXPLICACIONES
for pasada in range(cantidad_elementos):
    print(f"\n🔄 Pasada {pasada + 1}:")

    for indice in range(cantidad_elementos - 1):
        num_actual = vector_numeros[indice]
        num_siguiente = vector_numeros[indice + 1]

        print(f"Comparando {num_actual} (posición {indice}) con {num_siguiente} (posición {indice + 1})")

        if num_actual < num_siguiente:
            # Explicación en pantalla
            print(f"➡ Intercambiando: {num_actual} sube, {num_siguiente} baja")

            # Intercambio manual explicado
            auxiliar = vector_numeros[indice]                   # Guardamos el primero
            vector_numeros[indice] = vector_numeros[indice + 1] # El segundo va al lugar del primero
            vector_numeros[indice + 1] = auxiliar               # El primero (auxiliar) va al lugar del segundo

            print("➡ Resultado parcial:", vector_numeros)
        else:
            print("✔ No se intercambia")

print("\n✅ Vector final ordenado de mayor a menor:", vector_numeros)

