print("Control de carga de combustible")
print("Ingrese los litros por carga. Para finalizar, ingrese un número negativo.")

# Inicialización
carga = 0
cargaTotal = 0
contador = 0

# Ingreso y procesamiento
while True:
    carga = float(input("Ingrese carga (litros): "))
    if carga < 0:
        break
    if carga < 5:
        print("⚠️ Alerta: carga inferior a 5 litros (posible error o carga mínima)")
    cargaTotal += carga
    contador += 1

# Resultados
print("\n--- RESULTADOS ---")
print("Total cargado: ", cargaTotal, "litros")
print("Promedio por carga: ", round(cargaTotal / contador, 2), "litros")
