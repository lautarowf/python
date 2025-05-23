#Calculo de area
print("Seleccione la figura que desea para calcular su area: ")
print("1 - Circulo")
print("2 - Triangulo")
opcion = int(input(">"))
PI = 3.14
if opcion == 1:
    radio = float(input("Ingrese el radio: "))
    area_circulo = PI * (radio)**0.5
    print("Area: ", area_circulo)
elif opcion == 2:    
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area_triangulo = (base * altura) / 2
    print("Area: ", area_triangulo)
else :
    print("Opcion invalida")    