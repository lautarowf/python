#Clasificacion de edad en categorias
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Menor de edad")
elif edad >= 18 and edad <65:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")