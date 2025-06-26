PRECIO_COMBUSTIBLE = 132

litros = float(input("Ingrese cuántos litros desea cargar: "))

while litros < 1 or litros > 50:
    print("Error: Ingrese un valor entre 1 y 50.")
    litros = float(input("Ingrese cuántos litros desea cargar: "))

total_a_pagar = litros * PRECIO_COMBUSTIBLE
print("Total a pagar: $", total_a_pagar)
