# Lista con nombres de los equipos de trabajo
equipos = ["Frontend", "Backend", "QA", "DevOps"]

# Lista con nombres de los proyectos de software
proyectos = ["Proyecto A", "Proyecto B"]

# Matriz de horas trabajadas
# Cada fila representa un proyecto
# Cada columna representa las horas que un equipo trabajó en ese proyecto
# Por ejemplo: Proyecto A → Frontend=10h, Backend=20h, QA=5h, DevOps=8h
horas_trabajadas = [
    [10, 20, 5, 8],   # Proyecto A
    [15, 25, 10, 12]  # Proyecto B
]
# Variables para guardar el total máximo y su índice
max_horas = -1  # Empezamos con un valor que seguramente sea superado
indice_proyecto_max = -1  # Guardará el número de fila con más horas

# Recorremos la matriz por filas (cada fila = un proyecto)
for i in range(len(horas_trabajadas)):
    # Sumamos las horas de todos los equipos en ese proyecto
    suma = sum(horas_trabajadas[i])
    
    # Mostramos en pantalla esa suma
    print(f"{proyectos[i]}: {suma} horas")
    
    # Si esa suma es la mayor hasta ahora, la guardamos
    if suma > max_horas:
        max_horas = suma
        indice_proyecto_max = i
print(f"\n📌 Proyecto con más horas: {proyectos[indice_proyecto_max]} ({max_horas} horas)")
print("\n⏱️ Tiempo total invertido por equipo:")

# Recorremos por columnas (por cada equipo)
for j in range(len(equipos)):
    total_equipo = 0  # Acumulador de horas

    # Recorremos todas las filas (todos los proyectos)
    for i in range(len(horas_trabajadas)):
        total_equipo += horas_trabajadas[i][j]  # sumamos la celda correspondiente

    print(f"{equipos[j]}: {total_equipo} horas")
while True:
    print("\n¿Deseás agregar un nuevo proyecto? (s/n)")
    opcion = input().lower()
    if opcion != "s":
        break  # Salimos del bucle si no quiere agregar

    nuevo_nombre = input("Nombre del nuevo proyecto: ")
    proyectos.append(nuevo_nombre)  # Lo agregamos a la lista de nombres

    nueva_fila = []  # Nueva fila para la matriz
    for equipo in equipos:
        horas = int(input(f"Horas trabajadas por {equipo}: "))
        nueva_fila.append(horas)

    horas_trabajadas.append(nueva_fila)  # Agregamos la fila a la matriz
    print("✅ Proyecto agregado correctamente.")
print("\n🧾 Proyectos cargados:")
for i in range(len(proyectos)):
    print(f"{proyectos[i]}: {horas_trabajadas[i]}")
