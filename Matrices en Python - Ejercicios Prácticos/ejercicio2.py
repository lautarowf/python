cantidad_de_alumnos = int(input("Ingrese la cantidad de alumnos: "))
calificaciones = []
for alumnos_indice in range(cantidad_de_alumnos):
    nombre = str(input("Nombre del alumno: "))
    cantidad_de_asignaturas = int(input("Cantidad de asignaturas: "))
    lista_asignaturas = []
    for asignatura_indice in range(cantidad_de_asignaturas):
        nombre_asignatura = str(input(f"Ingrese la asignatura {asignatura_indice+1}: "))
        cantidad_notas = int(input("Ingrese las cantidad de notas de la asignatura: "))
        lista_notas = []
        for nota_indice in range(cantidad_notas):
            valor_nota = int(input(f"Ingrese la nota {nota_indice+1}: "))
            lista_notas.append(valor_nota)
        materia = [nombre_asignatura, lista_notas]
        lista_asignaturas.append(materia)
    alumno = [nombre, lista_asignaturas]
    calificaciones.append(alumno)
for alumno in calificaciones:
    print(alumno)

