PRECIO_COMBUSTIBLE = 132
litros = float(input("Ingrese cuantos litros desea cargar")
  while litros  < 1 and litros > 50:
      print("Ingrese un valor entre 1 y 50")
      litros = float(input("Ingrese cuantos litros desea cargar")
total_a_pagar = litros * PRECIO_COMBUSTIBLE
print("$", total_a_pagar)