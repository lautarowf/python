print("-------------------------------------------------------")
print("Complemento1: PRODUCTO VECTORIAL Y ESCALAR - Modo Depuración")
print("-------------------------------------------------------")

# Inicialización de los vectores
vector_1 = [0] * 3
vector_2 = [0] * 3

# Entrada de datos para el primer vector con depuración
print("\n🔹 Ingrese los valores del primer vector (vector_1):")
for posicion in range(3):
    vector_1[posicion] = int(input(f"vector_1[{posicion+1}]: "))
    print(f"➡️  vector_1 hasta ahora: {vector_1}")

# Entrada de datos para el segundo vector con depuración
print("\n🔹 Ingrese los valores del segundo vector (vector_2):")
for posicion in range(3):
    vector_2[posicion] = int(input(f"vector_2[{posicion+1}]: "))
    print(f"➡️  vector_2 hasta ahora: {vector_2}")

# Cálculo del Producto Escalar con depuración
producto_escalar = 0
print("\n🔹 Calculando Producto Escalar paso a paso:")
for posicion in range(3):
    parcial = vector_1[posicion] * vector_2[posicion]
    producto_escalar += parcial
    print(f"   - Multiplicación de vector_1[{posicion}] * vector_2[{posicion}] = {parcial}")
    print(f"   - Acumulado producto escalar: {producto_escalar}")

print("\n✅ Producto Escalar Final:", producto_escalar)

# Cálculo del Producto Vectorial con depuración
print("\n🔹 Calculando Producto Vectorial paso a paso:")

componente_x = vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1]
print(f"   - componente_x = ({vector_1[1]} * {vector_2[2]}) - ({vector_1[2]} * {vector_2[1]}) = {componente_x}")

componente_y = -(vector_1[0] * vector_2[2] - vector_1[2] * vector_2[0])
print(f"   - componente_y = -(({vector_1[0]} * {vector_2[2]}) - ({vector_1[2]} * {vector_2[0]})) = {componente_y}")

componente_z = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]
print(f"   - componente_z = ({vector_1[0]} * {vector_2[1]}) - ({vector_1[1]} * {vector_2[0]}) = {componente_z}")

print("\n✅ Producto Vectorial Final: {}i {}j {}k".format(componente_x, componente_y, componente_z))
