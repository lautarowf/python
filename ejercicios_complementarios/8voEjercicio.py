#Calcular el tiempo de encuentro
velocidadA = float(input("Ingrese la velocidad de A en km/h: "))
velocidadB = float(input("Ingrese la velocidad de B en km/h: "))
distancia = float(input("Ingrese la distancia que los separa en metros: "))
#Formula: Te= d/(v1 + v2)
velocidadA_en_metros = velocidadA*1000/3600
velocidadB_en_metros = velocidadB*1000/3600
tiempo_de_encuentro = distancia/(velocidadA_en_metros+velocidadB_en_metros)
print("El tiempo de encuentro es: ",round(tiempo_de_encuentro, 2), " segundos")