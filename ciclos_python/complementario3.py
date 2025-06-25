print("Verificador de números primos")

numero = int(input("Ingrese un número entero mayor que 1: "))
es_primo = True  # Suponemos que es primo

if numero <= 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break  # Ya encontramos un divisor, no hace falta seguir

if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
