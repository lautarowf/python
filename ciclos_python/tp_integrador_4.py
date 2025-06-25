contadorAlumnos = 0
contadorDesaprobados = 0
contadorAprobados = 0

print("Registro de notas de 10 alumnos")

while contadorAlumnos < 10:
    nota = int(input(f"Ingrese la nota del alumno {contadorAlumnos + 1}: "))
    if nota >= 6:
        contadorAprobados += 1
    else:
        contadorDesaprobados += 1
    contadorAlumnos += 1

print("\n--- RESULTADOS ---")
print("Aprobados:", contadorAprobados)
print("Desaprobados:", contadorDesaprobados)
