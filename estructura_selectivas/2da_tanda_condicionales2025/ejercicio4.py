#Descuento por tipo de cliente
print("Ingrese el tipo de cliente: (A, B o C)")
tipo_cliente = input()
if tipo_cliente == "A" or "a":
    print("20% de descuento")
elif tipo_cliente == "B" or "b":
    print("10% de descuento")
elif tipo_cliente == "C" or "c":
    print("0% de descuento")