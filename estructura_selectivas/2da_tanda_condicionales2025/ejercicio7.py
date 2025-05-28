#Estado de una lampara inteligente
print("Ingrese un color: ")
print("Rojo --> Ocupado")
print("Verde --> Disponible")
print("Azul --> En descanso")
estado_lampara = input().lower()
if estado_lampara == "rojo":
    print("Estado actual: Ocupado")
elif estado_lampara == "verde":
    print("Estado actual: Disponible")    
elif estado_lampara == "azul":
    print("Estado actual: En descanso")