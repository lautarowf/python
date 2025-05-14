#Calculos
calculo = int(input("elija el calculo: "))
numero = int(input("ingrese un numero: "))
funcion = {
1:100*numero,
2:100**numero,
3:100/numero
}
numero = funcion.get(calculo, 0)
print(numero)