#Area y Volumen de un cilindro 
print("Ingrese la altura del cilindro")
altura = float(input())
print("Ingrese el radio del cilindro")
radio = float(input())
pi = 3.1416
area = 2*pi*radio*(radio+altura)
volumen = pi*(radio**2)*altura
print("El area es: ",area, "y el volumen es: ", volumen)