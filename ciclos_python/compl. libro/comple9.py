entradas_general = 20
entradas_estudiante = 10
entradas_jubilado = 10
total_recaudado = 0

while entradas_general > 0 or entradas_estudiante > 0 or entradas_jubilado > 0:
    print("Seleccione su entrada")
    print("1. General")
    print("2. Estudiante")
    print("3. Jubilado")
    option = int(input())

    if option != 1 and option != 2 and option != 3:
        print("Error: opción inválida.")
    elif option == 1:
        if entradas_general > 0:
            entradas_general -= 1
            total_recaudado += 1500
        else:
            print("No quedan entradas generales.")
    elif option == 2:
        if entradas_estudiante > 0:
            entradas_estudiante -= 1
            total_recaudado += 1000
        else:
            print("No quedan entradas de estudiante.")
    elif option == 3:
        if entradas_jubilado > 0:
            entradas_jubilado -= 1
            total_recaudado += 800
        else:
            print("No quedan entradas de jubilado.")

print("Entradas agotadas.")
print("Total recaudado:", total_recaudado)
