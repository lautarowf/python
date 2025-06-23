# Decoración: Título del algoritmo
print("-------------------------------------------------------")
print("Complemento3: CUBO DE UN NÚMERO PRIMO.")
print("-------------------------------------------------------")

# Inicialización
numero_a_probar = 2               # Comenzamos a verificar desde el número 2
primos_encontrados = 0           # Contador de primos encontrados

# Proceso: Seguimos hasta encontrar 10 números primos
while primos_encontrados < 10:
    es_primo = True              # Suponemos que el número es primo

    # Verificamos si tiene divisores (no hace falta probar más allá de la mitad del número)
    for posible_divisor in range(2, numero_a_probar // 2 + 1):
        if numero_a_probar % posible_divisor == 0:
            es_primo = False     # Si tiene un divisor, no es primo
            break                # Ya sabemos que no es primo, cortamos el bucle

    # Si es primo, mostramos el cubo
    if es_primo:
        cubo = numero_a_probar ** 3
        print(f"El cubo de {numero_a_probar} es: {cubo}")
        primos_encontrados += 1  # Contamos este número primo

    # Pasamos al siguiente número
    numero_a_probar += 1
