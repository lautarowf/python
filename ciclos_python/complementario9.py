precio_total = 0
compra = "" 
compras_mas_1000 = 0
print("Bienvenido ingrese su compra (o 'Fin' para salir)")
while compra != "Fin":
    compra = str(input("Producto: "))
    if compra.lower() == "fin":
        break
    cantidad_de_productos = int(input("Cantidad: "))
    precio_unitario = int(input("Precio: "))
    precio_compra = cantidad_de_productos*precio_unitario
    if precio_compra > 1000:
        compras_mas_1000 += 1
    precio_total += precio_compra
print(f"Su total es $ {precio_total}")
print(f"{compras_mas_1000} superaron los $1000")