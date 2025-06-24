cantidad_de_empleados = 0
contador_de_sueldos = 0
sueldo_mayor = 0
orden_del_mayor = 0

print("Ingrese la cantidad de empleados: ")
cantidad_de_empleados = int(input())

while contador_de_sueldos < cantidad_de_empleados:
    print("Ingrese el sueldo: ")
    sueldo = int(input())
    contador_de_sueldos += 1

    if sueldo > sueldo_mayor:
        sueldo_mayor = sueldo
        orden_del_mayor = contador_de_sueldos

print("Empleado:", orden_del_mayor, "-", sueldo_mayor)
