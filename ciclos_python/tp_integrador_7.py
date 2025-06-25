print("Registro de temperaturas máximas semanales")
print("Ingrese la temperatura máxima de cada día:")

contador = 0
contadorMas30 = 0
sumaMaximas = 0

while contador < 7:
    temperatura = int(input(f"Día {contador + 1}: "))
    sumaMaximas += temperatura
    if temperatura > 30:
        contadorMas30 += 1
    contador += 1

media = sumaMaximas / 7

print("\n--- RESULTADOS ---")
print(contadorMas30, "días superaron los 30°C")
print("La media semanal fue:", round(media, 2), "°C")
