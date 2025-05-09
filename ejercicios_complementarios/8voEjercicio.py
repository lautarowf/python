#Calcular el tiempo de encuentro
velocidadA = float(input("Ingrese la velocidad de A: "))
velocidadB = float(input("Ingrese la velocidad de B: "))
distancia = float(input("Ingrese la distancia que los separa: "))
#Formula: Te= d/(v1 + v2)
tiempo_de_encuentro = distancia/(velocidadA+velocidadB)
print("El tiempo de encuentro es: ",round(tiempo_de_encuentro, 2), " segundos")