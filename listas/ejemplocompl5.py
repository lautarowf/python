tamanio = int(input("Tamanio de arreglo: "))
arreglo_numeros =[]
for i in range(tamanio):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    arreglo_numeros.append(numero)
numero_buscado = int(input("Numero a buscar: "))
for posicion in range(len(arreglo_numeros)):
    if numero_buscado == arreglo_numeros[posicion]:
        print(posicion+1)