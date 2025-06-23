# Decoración: Título del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio3: NÚMEROS PRIMOS ENTRE 1 Y 1000.")
print("-------------------------------------------------------")

# Constantes
numero_inicial = 2
numero_limite = 1000

# Inicialización
cantidad_primos = 0

# Proceso principal: revisar todos los números desde 2 hasta 999
for numero_actual in range(numero_inicial, numero_limite):
    es_primo = True  # Asumimos que el número es primo hasta que se pruebe lo contrario
    divisor = 2

    # Revisión de divisores desde 2 hasta (numero_actual - 1)
    while divisor < numero_actual and es_primo:
        if numero_actual % divisor == 0:
            # Si encontramos un divisor exacto (además del 1 o el mismo número), no es primo
            es_primo = False
            break  # Salimos del bucle porque ya sabemos que no es primo
        else:
            divisor += 1  # Probamos con el siguiente divisor

    # Si sigue siendo primo, lo imprimimos y contamos
    if es_primo:
        print(numero_actual, "es primo.")
        cantidad_primos += 1

# Salida final
print("\nSALIDA:")
print("-------------------------------------------------------")
print("Entre", numero_inicial, "y", numero_limite, "hay", cantidad_primos, "números primos.")
