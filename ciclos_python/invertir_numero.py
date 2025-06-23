print("-------------------------------------------------------")
print("Complemento6: INVERTIR NÚMERO.")
print("-------------------------------------------------------")

# Entrada: número a invertir
numero_original = int(input("Ingrese un número: "))

# Inicialización
numero_a_invertir = numero_original  # copia para manipular
numero_invertido = 0                  # resultado invertido

# Proceso: mientras queden dígitos por extraer
while numero_a_invertir > 0:
    digito = numero_a_invertir % 10               # extraer último dígito
    numero_invertido = numero_invertido * 10 + digito  # agregar dígito al invertido
    numero_a_invertir = numero_a_invertir // 10   # eliminar último dígito

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"El número invertido de {numero_original} es: {numero_invertido}")
