print("Suma de los dígitos de un número")

numero = int(input("Ingrese un número entero positivo: "))
suma_digitos = 0

while numero > 0:
    digito = numero % 10         # Último dígito
    suma_digitos += digito       # Se suma a la acumulación
    numero = numero // 10        # Se elimina el último dígito

print("La suma de los dígitos es:", suma_digitos)
