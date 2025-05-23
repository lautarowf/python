#tiempo de encuentro 
distancia = float(input("Ingrese la distancia que separa a ambos vehículos"))
velocidad_1 = float(input("Ingrese la velocidad del primer vehículo"))
velocidad_2 = float(input("Ingrese la velocidad del segundo vehículo"))
tiempo_de_encuentro = distancia/(velocidad_1 + velocidad_2)
if velocidad_1 > 0 and velocidad_2 > 0:
   print(tiempo_de_encuentro)
else:
   print(Error)


