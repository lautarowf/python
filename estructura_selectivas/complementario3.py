#Precio de estereos
print("Ingrese la marca de su producto: ")
marca_producto = input()
print("Ingrese el valor de su producto: ")
valor_producto = float(input())
if valor_producto >= 2000 :
    if marca_producto == "NOSY" or "nosy" or "Nosy":
        print((valor_producto*0.85)*1.20)
    else :
        print((valor_producto*0.90)*1.20)     
else :
    if marca_producto == "NOSY" or "nosy" or "Nosy":
        print((valor_producto*0.95)*1.20)
    else :
        print (valor_producto*1.20)        