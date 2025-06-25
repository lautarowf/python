numeros_positivos = 0
numeros_negativos = 0
ceros = 0

for i in range(20):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero > 0:
        numeros_positivos += 1
    elif numero < 0:
        numeros_negativos += 1
    else:
        ceros += 1

print("\n--- RESULTADOS ---")
print("Positivos:", numeros_positivos)
print("Negativos:", numeros_negativos)
print("Ceros:", ceros)
