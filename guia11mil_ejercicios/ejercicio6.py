numero = int(input("Ingrese el número para calcular su tabla de multiplicar: "))
hasta = int(input("Ingrese hasta qué número desea multiplicar: "))

contador = 1
while contador <= hasta:
    print(f"{numero} * {contador} = {numero * contador}")
    contador += 1
