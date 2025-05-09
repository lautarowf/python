#Convertir grados
Pi = 3.1416
angulo_radianes = float(input("Ingrese el angulo en radianes: "))
#Formulas: rad * 180/Pi ; rad * 200/Pi
angulo_sexagesimal = angulo_radianes*180/Pi
angulo_centesimal = angulo_radianes*200/Pi
print("El angulo en sexagesimales es: ",angulo_sexagesimal)
print("El angulo en centesimales es: ",angulo_centesimal)