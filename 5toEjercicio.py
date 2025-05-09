#Cantidad de Micro discos
import math
print("Ingrese la cantidad en que desea grabar (en GB)")
GB = float(input())
MB = GB * 1024
MicroDiscos = MB/1.44
print("Se necesitan ", math.ceil(MicroDiscos), "Micro discos 3.5")