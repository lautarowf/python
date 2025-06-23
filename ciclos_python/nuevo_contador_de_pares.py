# Decoración del algoritmo
print("-------------------------------------------------------")
print("Complemento11: CONTAR CUÁNTOS NÚMEROS SON PARES.")
print("-------------------------------------------------------")

# Inicialización de variables
cantidad_numeros = 100  # Total de números a ingresar
contador_pares = 0      # Contador de números pares ingresados
contador_entradas = 1   # Lleva la cuenta de cuántos números ya se ingresaron

# Entrada y proceso
print("Ingrese", cantidad_numeros, "números enteros:")

while contador_entradas <= cantidad_numeros:
    numero_ingresado = int(input(f"Ingrese el número {contador_entradas}: "))
    
    # Verificar si es par
    if numero_ingresado % 2 == 0:
        contador_pares += 1
    
    contador_entradas += 1

# Salida del resultado
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"En {cantidad_numeros} números enteros hay {contador_pares} números pares.")
