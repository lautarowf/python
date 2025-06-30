objetivo_diario = 0
for dias in range (1, 8):
  tiempo_entrenado =  float(input("Ingrese cantidad de minutos diarios de entrenamiento"))
   if tiempo_entrenado >= 30:
     objetivo_diario += 1
if objetivo_diario >= 5: 
   print("objetivo cumplido!")
else:
  print("no se logró el objetivo")