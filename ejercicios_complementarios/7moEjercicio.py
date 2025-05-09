#Calcular el lado restante del triagulo
import math
ladoB = float(input("Ingrese el lado b del triangulo: "))
ladoC = float(input("Ingrese el lado c del triangulo: "))
anguloBC = float(input("Ingrese el angulo que forman los lados a y b: "))
Pi = 3.1416
#formula a^2 = b^2 + c^2 - 2bc * cos(alfa)
ladoA = ((ladoB)**2 + (ladoC)**2 - 2*ladoB*ladoC * math.cos(anguloBC*Pi/180))**0.5
print("El lado a es: ", round(ladoA))