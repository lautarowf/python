tanque = 0
consumo_litro_por_km = 0.07  # Litros por kilómetro
precio_litro = 1100

print("Simulador de carga y consumo de combustible")
print("Ingrese cuánto desea cargar en pesos (ingrese 0 para detener):")

while True:
    carga_en_pesos = float(input("Carga ($): "))
    if carga_en_pesos == 0:
        break

    carga = carga_en_pesos / precio_litro  # Calculamos litros cargados
    tanque += carga
    print(f"Cargaste {carga:.2f} litros. Combustible total: {tanque:.2f} litros.\n")

# Cálculo de autonomía
km_posibles = tanque / consumo_litro_por_km
print(f"\nCon el combustible actual podés recorrer aproximadamente {km_posibles:.2f} km.")

# Verificación del mínimo necesario
if km_posibles < 50:
    print("⚠️ ¡No alcanza para recorrer 50 km! Cargá más combustible.")
else:
    print("✅ Tenés combustible suficiente para recorrer al menos 50 km.")
