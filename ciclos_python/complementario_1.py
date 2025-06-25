numeros_positivos = 0
numeros_negativos = 0
ceros = 0
cantidad_de_numeros = 0

while cantidad_de_numeros < 20:
    numero = int(input("Ingrese un número: "))
    
    if numero > 0:
        numeros_positivos += 1
    elif numero < 0:
        numeros_negativos += 1
    else:
        ceros += 1

    cantidad_de_numeros += 1

print("\n--- RESULTADOS ---")
print("Positivos:", numeros_positivos)
print("Negativos:", numeros_negativos)
print("Ceros:", ceros)
