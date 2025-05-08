#Respuestas y puntaje 
print("Ingrese la cantidad de respuestas correctas")
correctas = int(input())
print("Ingrese la cantidad de respuestas incorrectas")
incorrectas = int(input())
print("Ingrese la cantidad de respuestas en blanco")
blanco = int(input())
puntaje_correctas = correctas*3
puntaje_incorrectas = incorrectas*-1
puntaje_blanco = blanco*0
puntaje=puntaje_correctas+puntaje_incorrectas+puntaje_blanco
print("El puntaje es: ", puntaje)