cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "))
calificaciones = []
for alumnos in range(cantidad_de_alumnos):
    nombre = str(input("Nombre del alumno: "))
    cantidad_de_asignaturas = int(input("Cantidad de asignaturas: "))
    lista_asignaturas = []
    for asignatura_indice in range(cantidad_de_asignaturas):
        nombre_asignatura = str(input(f"Ingrese la asignatura {asignatura_indice+1}: "))
        lista_asignaturas.append(nombre_asignatura)
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))
    lista_notas = []
    for nota_indice in range(cantidad_notas):
        valor_nota = int(input(f"Ingrese la nota {nota_indice+1}: "))
        lista_notas.append(valor_nota)
    materias = [lista_asignaturas, lista_notas]
    alumno = [nombre, materias]
    calificaciones.append(alumno)
for alumno in calificaciones:
    print(alumno)
