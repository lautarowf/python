
# Algoritmo: Mostrar los dígitos de un número de derecha a izquierda

print("-------------------------------------------------------")
print("Ejercicio4: MOSTRAR DÍGITOS EN ORDEN INVERSO")
print("-------------------------------------------------------")

# Entrada del número
print("Introduce un número: ")
numero = int(input())

# Proceso: extraer y mostrar los dígitos desde el final
while numero > 0:
    digito = numero % 10          # Obtiene el último dígito
    print(digito)                 # Muestra el dígito
    numero = numero // 10         # Elimina el último dígito del número
