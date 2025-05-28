#Nivel de bateria
nivel_bateria = int(input("Ingrese el nivel de bateria: "))
if nivel_bateria == 100:
    print("Cargado completamente")
elif nivel_bateria >20 and nivel_bateria<100:
    print("Bateria adecuada")    
elif nivel_bateria <20:
    print("Bateria baja")