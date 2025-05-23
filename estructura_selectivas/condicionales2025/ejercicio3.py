#Menu de restaurante (if-elif-else)
print("Seleccione una opcion: ")
print("1. Hambuerguesa")
print("2. Pizza")
print("3. Ensalada")
print("4. Salir")
opcion = int(input())
if opcion == 1:
    print("Hoy comemos hamburguesas!")
elif opcion == 2:
    print("Hoy comemos pizza!")
elif opcion == 3:
    print("Hoy comemos ensalada!")
elif opcion == 4:
    print("Adios!")
else:
    print("Opcion invalida")    
        
#Menu de restaurante (match-case)
print("Seleccione una opcion: ")
print("1. Hambuerguesa")
print("2. Pizza")
print("3. Ensalada")
print("4. Salir")
opcion = int(input())
match opcion:
    case 1:
        print("Hoy comemos hamburguesas!")
    case 2:
        print("Hoy comemos pizza!")
    case 3:
        print("Hoy comemos ensalada!")
    case 4:
        print("Adios!")
    case _:
        print("Opcion invalida")