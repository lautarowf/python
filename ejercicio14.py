#Calculos
numero = int(input("ingrese un numero"))
calculo = int(input("elija el calculo"))
funcion = {
1:100*calculo
2:100**calculo
3:100/calculo
}
calculo = funcion.get(numero, 0)
print(calculo)