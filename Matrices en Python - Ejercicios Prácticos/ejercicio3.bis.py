# --- Datos de productos ---
pantalon = 15000
chaquetas = 12000
camisas = 10000
camperas = 20000
buzos = 15000
remeras = 8000

# Listas con nombres y precios
nombres = ["pantalon", "chaquetas", "camisas", "camperas", "buzos", "remeras"]
precios = [pantalon, chaquetas, camisas, camperas, buzos, remeras]
cantidad_productos = len(nombres)

# --- Ingreso de cantidad de sucursales ---
cantidad_sucursales = int(input("Ingrese la cantidad de sucursales: "))

# Matriz de ventas: filas = sucursales, columnas = productos
ventas_por_sucursal = [
    [0] * cantidad_productos for sucursal_indice in range(cantidad_sucursales)
]

# Lista para total recaudado por cada sucursal
recaudacion_por_sucursal = [0] * cantidad_sucursales

# --- Registro de ventas ---
while True:
    print("\nSeleccione la sucursal (1 a", cantidad_sucursales, "| 0 para salir):")
    numero_sucursal = int(input("Sucursal: "))

    if numero_sucursal == 0:
        break
    elif 1 <= numero_sucursal <= cantidad_sucursales:
        sucursal_indice = numero_sucursal - 1

        print("\nSeleccione el producto vendido:")
        for producto_indice in range(cantidad_productos):
            print(f"{producto_indice + 1} - {nombres[producto_indice]} (${precios[producto_indice]})")
        print("0 - Cancelar")

        numero_producto = int(input("Producto: "))
        if numero_producto == 0:
            continue
        elif 1 <= numero_producto <= cantidad_productos:
            producto_indice = numero_producto - 1

            # Registramos la venta
            ventas_por_sucursal[sucursal_indice][producto_indice] += 1
            recaudacion_por_sucursal[sucursal_indice] += precios[producto_indice]

            print(f"✅ Registrada venta en sucursal {numero_sucursal}: {nombres[producto_indice]} por ${precios[producto_indice]}")
        else:
            print("⚠️ Producto inválido")
    else:
        print("⚠️ Sucursal inválida")

# --- Informe 1: Producto más vendido por cada sucursal ---
print("\n--- Producto más vendido por cada sucursal ---")
for sucursal_indice in range(cantidad_sucursales):
    ventas_sucursal = ventas_por_sucursal[sucursal_indice]
    cantidad_maxima = max(ventas_sucursal)

    if cantidad_maxima > 0:
        indice_producto_mas_vendido = ventas_sucursal.index(cantidad_maxima)
        print(f"Sucursal {sucursal_indice + 1}: {nombres[indice_producto_mas_vendido]} ({cantidad_maxima} unidades)")
    else:
        print(f"Sucursal {sucursal_indice + 1}: No vendió ningún producto.")

# --- Informe 2: Sucursal con mayor recaudación ---
print("\n--- Sucursal con mayor recaudación ---")
monto_maximo = max(recaudacion_por_sucursal)
indice_sucursal_top = recaudacion_por_sucursal.index(monto_maximo)
print(f"Sucursal {indice_sucursal_top + 1} recaudó más: ${monto_maximo}")

# --- Informe 3: Promedio de unidades vendidas por producto ---
print("\n--- Promedio de unidades vendidas por producto (en todas las sucursales) ---")
for producto_indice in range(cantidad_productos):
    total_unidades_producto = 0
    for sucursal_indice in range(cantidad_sucursales):
        total_unidades_producto += ventas_por_sucursal[sucursal_indice][producto_indice]

    promedio_producto = total_unidades_producto / cantidad_sucursales
    print(f"{nombres[producto_indice]}: {promedio_producto:.2f} unidades por sucursal")
