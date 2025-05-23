#Dias de la semana laborales o no laborales
print("Seleccione una opcion: ")
print("1. Lunes")
print("2. Martes")
print("3. Miercoles")
print("4. Jueves")
print("5. Viernes")
print("6. Sabado")
print("7. Domingo")
opcion = int(input())
match opcion:
    case 1:
        print("Dia laboral")
    case 2:
        print("Dia laboral")
    case 3:
        print("Dia laboral")
    case 4:
        print("Dia laboral")
    case 5:
        print("Dia laboral")
    case 6:
        print("Fin de semana")
    case 7:
        print("Fin de semana")
    case _:
        print("Opcion invalida")