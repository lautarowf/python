#Respuestas y puntaje 
print("Ingrese la cantidad de respuestas correctas")
correctas = int(input())
print("Ingrese la cantidad de respuestas incorrectas")
incorrectas = int(input())
print("Ingrese la cantidad de respuestas en blanco")
blanco = int(input())
puntaje= correctas *3 + incorrectas * -1
print("El puntaje es: ", puntaje)