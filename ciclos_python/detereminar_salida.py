# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio4: DETERMINAR LA SALIDA.")
print("-------------------------------------------------------")
#Constantes
#Entradas
print("Introduce un número: ")
N = int( input())
while N > 0 :
    RESTO = N % 10
    print(RESTO)
    N = N // 10 #División Entera, N/10, es una división decimal