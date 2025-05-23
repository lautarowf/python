#Verificacion de velocidad permitida
velocidad = float(input("Ingrese la velocidad de su vehiculo: (km/h)"))
if velocidad < 61:
    print("Esta dentro del limite permitido")
elif velocidad < 81: 
    print("Esta en exceso leve")
else: 
    print("Esta en exceso grave")