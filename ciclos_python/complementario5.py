#Simulacion de carrito
cantidad_de_productos = 0
precio_total = 0

while item != "Salir":
    item = str(input("Ingrese su producto: "))
    cantidad_de_item = int(input("Ingrese la cantidad: "))
    precio_item = float(input("Ingrese el precio: "))
    cantidad_de_productos += cantidad_de_item
    precio_item = cantidad_de_item*precio_item
    precio_total += precio_item
print(f"Su carrito cuenta con {cantidad_de_productos} productos")

print(f"Su carrito acumula un total de: $ {precio_total}")