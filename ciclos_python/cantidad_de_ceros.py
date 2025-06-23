# Decoración
print("-------------------------------------------------------")
print("Complemento8: CONTAR CUÁNTOS CEROS HAY EN UNA LISTA DE NÚMEROS")
print("-------------------------------------------------------")

# Entrada
cantidad_numeros = int(input("Ingrese la cantidad de números a evaluar: "))

# Inicializar contador de ceros
cantidad_ceros = 0

# Proceso
for posicion in range(1, cantidad_numeros + 1):
    numero_ingresado = int(input(f"Ingrese el número {posicion}: "))
    if numero_ingresado == 0:
        cantidad_ceros += 1

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("Hay", cantidad_ceros, "número(s) igual(es) a cero.")
