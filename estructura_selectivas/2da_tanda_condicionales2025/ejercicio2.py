#Comprobacion de precios entre dos productos
producto_1 = float(input("Ingrese el precio del primer producto: "))
producto_2 = float(input("Ingrese el precio del segundo producto: "))
if producto_1 == producto_2:
    print("Cuestan lo mismo")
elif producto_1 > producto_2:
    print("Conviene el segundo producto")
else:
    print("Conviene el primer producto")    