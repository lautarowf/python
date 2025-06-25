stock = 100
stockInicial = stock  # Para calcular el 10% después

print("CONTROL DE STOCK")
print("Ingrese la cantidad de productos vendidos (ingrese 0 para finalizar)")

while stock > 0:
    productosVendidos = int(input("Vendidos: "))
    
    if productosVendidos == 0:
        break
    
    if productosVendidos > stock:
        print("⚠️ No hay suficiente stock. Solo quedan", stock, "productos.")
        continue

    stock -= productosVendidos

    if stock < stockInicial * 0.10:
        print("⚠️ Alerta: queda menos del 10% del stock original")

print("Stock restante:", stock)
