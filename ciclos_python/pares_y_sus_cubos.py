# Decoración: Nombre del Algoritmo 
print("-------------------------------------------------------")
print("Complemento2: PARES Y SUS CUBOS.")
print("-------------------------------------------------------")

# Proceso
numero_inicial = 2
numero_final = 20
incremento = 2  # Vamos de a pares

for numero_par in range(numero_inicial, numero_final + 1, incremento):
    cubo = numero_par ** 3
    print(f"El cubo de {numero_par} es {cubo}")
