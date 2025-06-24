# Decoración: Título del Algoritmo
print("-------------------------------------------------------")
print("Complemento12: IMPRIMIR PARES Y SUS CUBOS.")
print("-------------------------------------------------------")

# Inicialización de variables
numero_actual = 2  # Empezamos con el primer número par
ultimo_par = 20    # Queremos llegar hasta el 20 porque es el décimo número par

# Proceso: mientras el número actual sea menor o igual a 20
while numero_actual <= ultimo_par:
    
    # Calcular el cubo del número actual
    cubo = numero_actual ** 3
    
    # Imprimir el número par y su cubo
    print("El cubo de", numero_actual, "es:", cubo)
    
    # Avanzar al siguiente número par
    numero_actual = numero_actual + 2
