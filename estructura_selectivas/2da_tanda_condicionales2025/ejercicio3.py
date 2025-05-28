#Clasificacion de la calidad del aire
indice_calidad_aire = float(input("Ingrese el valor del indice de calidad del aire (ICA): "))
if indice_calidad_aire < 50:
    print("Bueno")
elif indice_calidad_aire < 100:
    print("Moderado")    
elif indice_calidad_aire >= 100:
    print("Peligroso")