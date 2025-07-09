# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento3: CRIBA DE ERATÓSTENES.")
print("-------------------------------------------------------")

# Inicialización:
# Lista de números del 1 al 100
lista_numeros = []
for numero in range(1, 101):
    lista_numeros.append(numero)

# Lista de banderas: al principio todos los números son considerados primos
es_primo = [True] * 100

# El número 1 no es primo (posición 0)
es_primo[0] = False

# Proceso: Criba de Eratóstenes
for posicion_actual in range(1, 100):  # Comienza desde la posición 1 (número 2)
    if es_primo[posicion_actual]:
        for siguiente_posicion in range(posicion_actual + 1, 100):
            if lista_numeros[siguiente_posicion] % lista_numeros[posicion_actual] == 0:
                es_primo[siguiente_posicion] = False  # Marcar como no primo

# Salida: Mostrar números que quedaron como primos
print("\n✅ Los números primos del 1 al 100 son:")
for posicion in range(100):
    if es_primo[posicion]:
        print(lista_numeros[posicion], end=" ")
