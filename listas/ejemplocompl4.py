lista_de_numeros = []
tamaño_maximo = 100
while True:
    print("1.- Añadir un elemento al vector")
    print("2.- Eliminar un elemento del vector")
    print("3.- Listar el contenido del vector")
    print("4.- Contar las apariciones de un número en el vector")
    print("5.- Calcular la media y el máximo de los elementos del vector")
    print("0.- Terminar")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        if len(lista_de_numeros) < tamaño_maximo:
            numero = int(input("Ingrese un número para añadir: "))
            lista_de_numeros.append(numero)
            print("Número añadido con éxito.")
        else:
            print("El vector está lleno. No se puede añadir más elementos.")
    elif opcion == 2:
        if lista_de_numeros:
            numero = int(input("Ingrese el número a eliminar: "))
            if numero in lista_de_numeros:
                lista_de_numeros.remove(numero)
                print("Número eliminado.")
            else:
                print("El número no está en el vector.")
        else:
            print("El vector está vacío. No se puede eliminar ningún elemento.")
    elif opcion == 3:
        if lista_de_numeros:
            print("Contenido del vector:", lista_de_numeros)
        else:
            print("El vector está vacío.")
    elif opcion == 4:
        if lista_de_numeros:
            numero = int(input("Ingrese el número para contar sus apariciones: "))
            apariciones = lista_de_numeros.count(numero)
            print(f"El número {numero} aparece {apariciones} veces.")
        else:
            print("El vector está vacío.")
    elif opcion == 5:
        if lista_de_numeros:
            suma = sum(lista_de_numeros)
            media = suma / len(lista_de_numeros)
            maximo = max(lista_de_numeros)
            print(f"Media: {media}")
            print(f"Máximo: {maximo}")
        else:
            print("El vector está vacío.")
    elif opcion == 6:
        print("Programa terminado.")
        break
    else:
        print("Error")        