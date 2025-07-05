# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento1: PRODUCTO VECTORIAL Y ESCALAR.")
print("-------------------------------------------------------")

# Inicialización de vectores vacíos
vector_1 = [0] * 3
vector_2 = [0] * 3

# Entrada de datos para el primer vector
print("Ingrese los 3 valores del primer vector (vector_1):")
for posicion in range(3):
    vector_1[posicion] = int(input(f"vector_1[{posicion+1}]: "))

# Entrada de datos para el segundo vector
print("Ingrese los 3 valores del segundo vector (vector_2):")
for posicion in range(3):
    vector_2[posicion] = int(input(f"vector_2[{posicion+1}]: "))

# Cálculo del Producto Escalar
producto_escalar = 0
for posicion in range(3):
    producto_escalar += vector_1[posicion] * vector_2[posicion]

print("El producto escalar es:", producto_escalar)

# Cálculo del Producto Vectorial (cada componente)
componente_x = vector_1[1] * vector_2[2] - vector_1[2] * vector_2[1]
componente_y = -(vector_1[0] * vector_2[2] - vector_1[2] * vector_2[0])
componente_z = vector_1[0] * vector_2[1] - vector_1[1] * vector_2[0]

print(f"El producto vectorial es: {componente_x}i {componente_y}j {componente_z}k")