#Estado de una lampara inteligente
print("Ingrese un color: ")
print("Rojo --> Ocupado")
print("Verde --> Disponible")
print("Azul --> En descanso")
estado_lampara = input()
if estado_lampara == "Rojo" or "ROJO" or "rojo":
    print("Estado actual: Ocupado")
elif estado_lampara == "Verde" or "VERDE" or "verde":
    print("Estado actual: Disponible")    
elif estado_lampara == "Azul" or "AZUL" or "azul":
    print("Estado actual: En descanso")