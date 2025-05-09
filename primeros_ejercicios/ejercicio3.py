#Calcular puntaje
print("Ingrese cantidad de respuestas correctas:")
respuestas_correctas = int(input())
print("Ingrese cantidad de respuestas incorrectas:")
respuestas_incorrectas = int(input())
print("Ingrese cantidad de respuestas en blanco:")
respuestas_blanco = int(input())
puntaje_correctas = respuestas_correctas*3
puntaje_incorrectas = respuestas_incorrectas*-1
puntaje_blanco = respuestas_blanco*0
puntaje = puntaje_blanco + puntaje_correctas + puntaje_incorrectas
print("Su puntaje es de: ", puntaje)