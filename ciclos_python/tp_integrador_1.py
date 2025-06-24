print("GASTOS MENSUALES")
print("Ingrese uno por uno sus gastos (ingrese un número negativo para terminar):")

TOPE = 100000  # Límite presupuestado
gasto = 0
gasto_total = 0

# Primera lectura antes del while
gasto = int(input("Ingrese un gasto: "))

while gasto >= 0:
    gasto_total += gasto
    gasto = int(input("Ingrese otro gasto (o negativo para salir): "))

print(f"\nTotal gastado: ${gasto_total}")

if gasto_total > TOPE:
    print(f"¡Atención! Sobrepasaste el límite presupuestado por ${gasto_total - TOPE}")
else:
    print(f"Aún estás dentro del presupuesto. Te quedan ${TOPE - gasto_total}")
