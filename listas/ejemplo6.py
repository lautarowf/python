# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Matriz3: ANÁLISIS DE VENTAS DE SUCURSALES")
print("-------------------------------------------------------")

# Inicialización
matriz_ventas = []

# Entradas
print("Ingrese número de sucursales y número de años:")
cantidad_sucursales = int(input("Número de Sucursales: "))
cantidad_anios = int(input("Número de Años: "))

# Cargar la matriz de ventas
for anio in range(cantidad_anios):
    matriz_ventas.append([])  # Agregar fila vacía para el año
    for sucursal in range(cantidad_sucursales):
        venta = int(input(f"Ingrese ventas de la Sucursal {sucursal + 1} en el Año {anio + 1}: "))
        matriz_ventas[anio].append(venta)

# PROCESO 1: Sucursal con más ventas totales
print("\nANÁLISIS: SUCURSAL CON MÁS VENTAS")
print("-------------------------------------------------------")

mayor_ventas_total = 0
sucursal_mas_vendedora = 0

for sucursal in range(cantidad_sucursales):
    suma_ventas_sucursal = 0
    for anio in range(cantidad_anios):
        suma_ventas_sucursal += matriz_ventas[anio][sucursal]
    
    print(f"Total de ventas de la Sucursal {sucursal + 1}: {suma_ventas_sucursal}")
    
    if suma_ventas_sucursal > mayor_ventas_total:
        mayor_ventas_total = suma_ventas_sucursal
        sucursal_mas_vendedora = sucursal + 1  # +1 porque el índice empieza en 0

print(f"Sucursal que más vendió: Sucursal {sucursal_mas_vendedora}")

# PROCESO 2: Año con mayor promedio de ventas
print("\nANÁLISIS: AÑO CON MEJOR PROMEDIO DE VENTAS")
print("-------------------------------------------------------")

mayor_promedio_ventas = 0
anio_mejor_promedio = 0

for anio in range(cantidad_anios):
    suma_ventas_anio = 0
    for sucursal in range(cantidad_sucursales):
        suma_ventas_anio += matriz_ventas[anio][sucursal]
    
    promedio_ventas_anio = suma_ventas_anio / cantidad_sucursales
    print(f"Promedio de ventas del Año {anio + 1}: {promedio_ventas_anio:.2f}")
    
    if promedio_ventas_anio > mayor_promedio_ventas:
        mayor_promedio_ventas = promedio_ventas_anio
        anio_mejor_promedio = anio + 1  # +1 para que se lea como Año 1, Año 2, etc.

print(f"Año con mayor promedio de ventas: Año {anio_mejor_promedio}")
