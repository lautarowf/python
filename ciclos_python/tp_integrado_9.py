LIMITE = 20000
compra = 0
compra_total = 0

print("Simulador de compras (límite diario: $20.000)")

while compra_total < LIMITE:
    compra = float(input("Ingrese el valor de su compra: "))
    
    if compra_total + compra > LIMITE:
        print("⚠️ No puede realizar esta compra. Supera el límite diario de $20.000.")
        break
    
    compra_total += compra
    print(f"Total acumulado: ${compra_total:.2f}")

print("Fin del día. Total gastado:", compra_total)
