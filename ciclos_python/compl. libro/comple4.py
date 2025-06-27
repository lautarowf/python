# Acumuladores de cantidad
alimentos = 0
transporte = 0
ocio = 0
otros = 0

# Acumuladores de montos
alimentos_gastos = 0
transporte_gastos = 0
ocio_gastos = 0
otros_gastos = 0

print("Registro de gastos - Ingrese 0 como monto para finalizar")

# Ciclo principal
while True:
    print("\nSeleccione la categoría del gasto:")
    print("1. Alimentos")
    print("2. Transporte")
    print("3. Ocio")
    print("4. Otros")

    opcion = int(input("Opción: "))
    
    if opcion not in [1, 2, 3, 4]:
        print("Opción inválida.")
        continue

    monto = float(input("Ingrese el monto (0 para finalizar): "))
    
    if monto == 0:
        break

    if opcion == 1:
        alimentos += 1
        alimentos_gastos += monto
    elif opcion == 2:
        transporte += 1
        transporte_gastos += monto
    elif opcion == 3:
        ocio += 1
        ocio_gastos += monto
    elif opcion == 4:
        otros += 1
        otros_gastos += monto

# Resultados
print("\n--- RESUMEN DE GASTOS ---")
if alimentos > 0:
    print(f"Alimentos: {alimentos} gastos - Total: ${alimentos_gastos:.2f} - Promedio: ${alimentos_gastos / alimentos:.2f}")
else:
    print("Alimentos: Sin registros")

if transporte > 0:
    print(f"Transporte: {transporte} gastos - Total: ${transporte_gastos:.2f} - Promedio: ${transporte_gastos / transporte:.2f}")
else:
    print("Transporte: Sin registros")

if ocio > 0:
    print(f"Ocio: {ocio} gastos - Total: ${ocio_gastos:.2f} - Promedio: ${ocio_gastos / ocio:.2f}")
else:
    print("Ocio: Sin registros")

if otros > 0:
    print(f"Otros: {otros} gastos - Total: ${otros_gastos:.2f} - Promedio: ${otros_gastos / otros:.2f}")
else:
    print("Otros: Sin registros")
