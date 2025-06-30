pedidos_almuerzo = 0
pedidos_cena = 0

hora = int(input("Hora (0 a 24): "))

while hora >= 0 and hora <= 24:
    if hora >= 12 and hora <= 15:
        print("Horario de almuerzo. Indique su pedido:")
        plato_principal = input("Plato principal: ")
        bebida = input("Bebida: ")
        postre = input("Postre: ")
        pedidos_almuerzo += 1

    elif hora >= 20 and hora <= 23:
        print("Horario de cena. Indique su pedido:")
        plato_principal = input("Plato principal: ")
        bebida = input("Bebida: ")
        postre = input("Postre: ")
        pedidos_cena += 1

    else:
        print("Fuera de horario. Pedido rechazado.")

    hora = int(input("Hora (0 a 24): "))  # volver a pedir hora

print("Cantidad de pedidos durante el almuerzo:", pedidos_almuerzo)
print("Cantidad de pedidos durante la cena:", pedidos_cena)
