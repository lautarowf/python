# Acumuladores
motor_con_turno = 0
frenos_con_turno = 0
pintura_con_turno = 0
motor_sin_turno = 0
frenos_sin_turno = 0
pintura_sin_turno = 0

# Ingreso inicial
tiene_turno = input("¿Tiene turno (S/N)? ").upper()

# Bucle principal
while tiene_turno == "S" or tiene_turno == "N":
    print("Seleccione una opción: ")
    print("1. Motor")
    print("2. Frenos")
    print("3. Pintura")
    opcion = int(input("Ingrese la opción: "))

    if tiene_turno == "S":
        if opcion == 1:
            motor_con_turno += 1
        elif opcion == 2:
            frenos_con_turno += 1
        elif opcion == 3:
            pintura_con_turno += 1
        else:
            print("Opción incorrecta.")
    elif tiene_turno == "N":
        if opcion == 1:
            motor_sin_turno += 1
        elif opcion == 2:
            frenos_sin_turno += 1
        elif opcion == 3:
            pintura_sin_turno += 1
        else:
            print("Opción incorrecta.")

    # Preguntar por el siguiente auto
    tiene_turno = input("¿Tiene turno el próximo auto? (S/N, otro para salir): ").upper()

# Mostrar resultados
print("\n----- RESUMEN DE LA JORNADA -----")
print("Motor con turno:", motor_con_turno)
print("Frenos con turno:", frenos_con_turno)
print("Pintura con turno:", pintura_con_turno)
print("Motor sin turno:", motor_sin_turno)
print("Frenos sin turno:", frenos_sin_turno)
print("Pintura sin turno:", pintura_sin_turno)
