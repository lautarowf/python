# -*- coding: utf-8 -*-
# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Algoritmo: Interacción con un Vector mediante un Menú de Opciones")
print("-------------------------------------------------------")

# Inicialización
vector_numeros = [0] * 100  # Vector con espacio para 100 elementos
cantidad_actual_numeros = 0  # Cantidad real de números ingresados

# Entrada: Tamaño máximo del vector
print("Ingrese el tamaño máximo que tendrá el vector:")
tamanio_maximo_vector = int(input())

opcion_menu = -1

while opcion_menu != 0:
    print("\n-------------------------------------------------------")
    print("MENÚ DE OPCIONES")
    print("1 - Añadir un número al vector")
    print("2 - Eliminar un número del vector")
    print("3 - Listar los números del vector")
    print("4 - Contar cuántas veces aparece un número en el vector")
    print("5 - Calcular la media y el valor máximo del vector")
    print("0 - Terminar el programa")

    opcion_menu = int(input("Seleccione una opción: "))

    if opcion_menu == 1:
        if cantidad_actual_numeros < tamanio_maximo_vector:
            numero_a_agregar = int(input("Ingrese un número para añadir al vector: "))
            vector_numeros[cantidad_actual_numeros] = numero_a_agregar
            cantidad_actual_numeros += 1
            print("Número añadido correctamente.")
        else:
            print("El vector está lleno. No se pueden añadir más números.")

    elif opcion_menu == 2:
        if cantidad_actual_numeros == 0:
            print("El vector está vacío. No se puede eliminar ningún número.")
        else:
            numero_a_eliminar = int(input("Ingrese el número que desea eliminar: "))
            numero_encontrado = False
            for posicion_busqueda in range(cantidad_actual_numeros):
                if vector_numeros[posicion_busqueda] == numero_a_eliminar:
                    numero_encontrado = True
                    for posicion_desplazamiento in range(posicion_busqueda, cantidad_actual_numeros - 1):
                        vector_numeros[posicion_desplazamiento] = vector_numeros[posicion_desplazamiento + 1]
                    vector_numeros[cantidad_actual_numeros - 1] = 0  # Limpiar última posición
                    cantidad_actual_numeros -= 1
                    print(f"El número {numero_a_eliminar} fue eliminado.")
                    break
            if not numero_encontrado:
                print(f"El número {numero_a_eliminar} no se encuentra en el vector.")

    elif opcion_menu == 3:
        if cantidad_actual_numeros > 0:
            print("Números actuales en el vector:")
            for posicion_listado in range(cantidad_actual_numeros):
                print(vector_numeros[posicion_listado], end=" ")
            print()
        else:
            print("El vector está vacío.")

    elif opcion_menu == 4:
        if cantidad_actual_numeros > 0:
            numero_a_contar = int(input("Ingrese el número para contar apariciones: "))
            cantidad_apariciones = 0
            for posicion_conteo in range(cantidad_actual_numeros):
                if vector_numeros[posicion_conteo] == numero_a_contar:
                    cantidad_apariciones += 1
            print(f"El número {numero_a_contar} aparece {cantidad_apariciones} veces en el vector.")
        else:
            print("El vector está vacío.")

    elif opcion_menu == 5:
        if cantidad_actual_numeros > 0:
            suma_total_numeros = 0
            valor_maximo_vector = vector_numeros[0]
            for posicion_calculo in range(cantidad_actual_numeros):
                suma_total_numeros += vector_numeros[posicion_calculo]
                if vector_numeros[posicion_calculo] > valor_maximo_vector:
                    valor_maximo_vector = vector_numeros[posicion_calculo]
            media_vector = suma_total_numeros / cantidad_actual_numeros
            print(f"El número máximo es: {valor_maximo_vector}")
            print(f"La media de los números es: {round(media_vector, 2)}")
        else:
            print("El vector está vacío. No se pueden calcular valores.")

    elif opcion_menu == 0:
        print("FIN DEL PROGRAMA. ¡Gracias por utilizar el sistema!")

    else:
        print("Opción inválida. Por favor, elija una opción válida.")