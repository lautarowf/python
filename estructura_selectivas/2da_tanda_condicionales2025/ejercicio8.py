#Clasificacion de un alimento segun calorias
cantidad_de_calorias = float(input("Ingrese las calorias del alimento: "))
if cantidad_de_calorias < 100:
    print("Ligero")
elif cantidad_de_calorias < 300:
    print("Moderado")
elif cantidad_de_calorias >= 300:
    print("Calórico")    