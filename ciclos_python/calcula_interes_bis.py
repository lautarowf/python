# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio1: CALCULA EL INTERÉS.")
print("-------------------------------------------------------")
#Inicialización
C = -1
I = 0
M = 0
#Entradas
while (C<0) or (I<=0) or (I>=100) or (M <=0):
print("Introduce el capital, el interés y el tiempo apropiados")
C = int( input("Capital: "))
I = int( input("Interés: "))
M = int( input("Tiempo en Años: "))
#Proceso
for i in range(M):
C = C*( 1 + I/100)
#Salida
print("\nSALIDA: ")
print("-------------------------------------------------------")
print ("Tienes", C , "soles")