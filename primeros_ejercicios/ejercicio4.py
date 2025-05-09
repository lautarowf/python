#Puntaje de Independiente
print("Ingrese la cantidad de partidos ganados:")
ganados = int(input())
print("Ingrese la cantidad de empates:")
empatados = int(input())
print("Ingrese la cantidad de partidos perdidos:")
perdidos = int(input())
puntaje_ganados = ganados*3
puntaje_empate = empatados*1
puntaje_perdidos = perdidos*0
puntaje = puntaje_empate + puntaje_ganados + puntaje_perdidos
print("El puntaje de Independiente es: ", puntaje)