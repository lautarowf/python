#Distancia entre dos puntos en el espacio 
print("Ingrese las coordenadas del punto 1")
x1 = float(input("x1= "))
y1 = float(input("y1= "))
z1 = float(input("z1= "))
print("Ingrese las coordenadas del punto 2")
x2 = float(input("x2= "))
y2 = float(input("y2= "))
z2 = float(input("z2= "))
#formula: d= ((x2 - x1)^2 + (y2 - y1)^2 +(z2 -z1)^2)^0.5
distancia = ((x2 - x1)**2 + (y2 - y1)**2 +(z2 -z1)**2)**0.5
print("La distancia entre el punto 1 y el punto 2 es: ",round(distancia, 2))