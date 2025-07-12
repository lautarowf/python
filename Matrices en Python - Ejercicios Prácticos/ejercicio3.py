pantalon = 15000
chaquetas = 12000
camisas = 10000
camperas = 20000
buzos = 15000
remeras = 8000
nombres = ["pantalon", "chaquetas", "camisas", "camperas", "buzos", "remeras"]
precios = [pantalon, chaquetas, camisas, camperas, buzos, remeras]
cantidades = [0] * len(nombres)
total_ventas = 0

while True:
    print("Seleccione el producto vendido: ")
    for producto_indice in range(len(nombres)):
        print(f"{producto_indice+1} - {nombres[producto_indice]} ${precios[producto_indice]}")
    print("0 - Salir")
    opcion_productos = int(input())
    if opcion_productos == 0:
        break
    elif 1 <= opcion_productos <= len(nombres):
        indice = opcion_productos - 1
        cantidades[indice] += 1
        total_ventas += precios[indice]
    else:
        print("Opcion invalida")
total_unidades = 0
for productos_indice in range(len(nombres)):
    print(f"{nombres[productos_indice]}: {cantidades[productos_indice]} unidades vendidas")
    total_unidades += cantidades[productos_indice]
print(f"Total: ${total_ventas}")

if total_unidades > 0:
    max_vendido = max(cantidades)
    indice_mas_vendido = cantidades.index(max_vendido)
    print(f"Producto más vendido: {nombres[indice_mas_vendido]} ({max_vendido} unidades)")
