# Decoración del algoritmo
print("-------------------------------------------------------")
print('Complemento10: CUÁNTAS VECES SE REPITE "a".')
print("-------------------------------------------------------")

# Inicialización del contador
cantidad_de_a = 0

# Entrada: cantidad de caracteres a ingresar
total_caracteres = 50

print("Ingrese", total_caracteres, "caracteres (uno por uno):")

# Proceso: bucle para ingresar los caracteres
for posicion in range(1, total_caracteres + 1):
    caracter_ingresado = input(f"Ingrese el carácter {posicion}: ")
    
    # Contar si es una 'a'
    if caracter_ingresado == "a":
        cantidad_de_a += 1

# Salida del resultado
print("\nSALIDA:")
print("-------------------------------------------------------")
print("En", total_caracteres, "caracteres hay", cantidad_de_a, "caracteres 'a'.")
