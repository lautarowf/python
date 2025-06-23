# Decoración
print("-------------------------------------------------------")
print("Complemento9: DETERMINA EL MAYOR Y MENOR.")
print("-------------------------------------------------------")

# Entrada: Pedimos cuántos números se van a comparar
print("Ingrese la cantidad de números a comparar:")
cantidad_numeros = int(input())

# Ingreso del primer número
print("Ingrese los números:")
primer_numero = int(input("Ingrese número 1: "))

# Inicialización de variables
numero_menor = primer_numero
numero_mayor = primer_numero

# Bucle para los siguientes N-1 números
for posicion in range(2, cantidad_numeros + 1):
    numero_actual = int(input(f"Ingrese número {posicion}: "))

    if numero_actual < numero_menor:
        numero_menor = numero_actual
    elif numero_actual > numero_mayor:
        numero_mayor = numero_actual

# Salida: Se imprime el menor y el mayor
print("\nSALIDA:")
print("-------------------------------------------------------")
print("El número menor es:", numero_menor)
print("El número mayor es:", numero_mayor)
