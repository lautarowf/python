#Distancia entre dos puntos
print("Ingrese la coordenada X del punto a")
aX = float(input())
print("Ingrese la coordenada Y del punto a")
aY = float(input())
print("Ingrese la coordenada X del punto b")
bX = float(input())
print("Ingrese la coordenada Y del punto b")
bY = float(input())
distancia = ((bX-aX)**2 + (bY-aY)**2)**0.5
print("La distancia entre el punto a y el punto b es: ", round(distancia, 2))