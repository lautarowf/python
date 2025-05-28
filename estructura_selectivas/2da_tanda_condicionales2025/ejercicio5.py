#Clasificacion de una bebida segun su temperatura
temperatura = float(input("Ingrese la temperatura de la bebida (C°): "))
if temperatura < 5:
    print("Fria")
elif temperatura < 20:
    print("Templada")    
elif temperatura >= 20:
    print("Caliente")