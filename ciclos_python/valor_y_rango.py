# Decoración del algoritmo
print("-------------------------------------------------------")
print("Ejercicio6: DETERMINAR VALOR Y RANGO MAYOR A 300.")
print("-------------------------------------------------------")

# Inicialización de los primeros dos valores de la secuencia
valor_anterior = 1            # Equivale a A1
valor_antes_anterior = 0      # Equivale a A2
termino_actual = valor_anterior + 2 * valor_antes_anterior  # An
cantidad_terminos = 0         # Contador de términos antes de superar 300

# Generar la secuencia mientras el término actual sea menor que 300
while termino_actual < 300:
    valor_antes_anterior = valor_anterior
    valor_anterior = termino_actual
    termino_actual = valor_anterior + 2 * valor_antes_anterior
    cantidad_terminos += 1

# Salida final
print("\nSALIDA:")
print("-------------------------------------------------------")
print("El rango es:", cantidad_terminos, "y el resultado es:", termino_actual)
