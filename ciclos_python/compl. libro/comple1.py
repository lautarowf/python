materia = ""
asistencia = ""
presentes = 0
ausentes = 0
materia = str(input("Ingrese la materia: "))
cantidad_de_clases = int(input("Ingrese cantidad de clases"))
for i in range(cantidad_de_clases):
        asistencia = str(input("P/A"))
        if asistencia.lower() == "p":
            presentes += 1
        elif asistencia.lower() == "a":
            ausentes += 1
if ((presentes / cantidad_de_clases) * 100) > 75:
    print("Aprobado")
else:
    print("Desaprobado")  