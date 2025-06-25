print("Simulación de colecta")
print("Ingrese los montos donados. Ingrese 0 para finalizar.")

contador = 0
totalRecaudado = 0
donacionMaxima = 0
donacion = 1  # Inicializamos con algo distinto de 0 para entrar al bucle

while donacion != 0:
    donacion = int(input("Ingrese el monto de su donación: "))
    
    if donacion == 0:
        break

    totalRecaudado += donacion
    contador += 1

    if donacion > donacionMaxima:
        donacionMaxima = donacion

print("\n--- RESULTADOS DE LA COLECTA ---")
print("Total recaudado: $", totalRecaudado)
print("Cantidad de donantes:", contador)
print("Mayor donación: $", donacionMaxima)
