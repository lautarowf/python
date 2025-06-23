
# Algoritmo: Aproximar e^x usando una serie de Taylor

print("-------------------------------------------------------")
print("Ejercicio5: CALCULANDO e^x.")
print("-------------------------------------------------------")

# Entrada
print("Ingrese el valor de x: ")
valor_x = int(input())

# Inicialización
resultado_e = 1         # e^x comienza en 1 (término 0 de la serie)
potencia = 1            # x^0 inicialmente
factorial = 1           # 0! = 1
termino = 1             # primer término (para entrar al bucle)
indice = 1              # comienza desde el término 1

# Bucle tipo "do while" simulando con while
while termino >= 0.000001:
    potencia = valor_x ** indice       # x^i
    factorial = factorial * indice     # i!
    termino = potencia / factorial     # término actual
    resultado_e += termino             # sumamos el término a e^x
    indice += 1                        # siguiente término

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print(f"e elevado a {valor_x} es aproximadamente: {resultado_e}")
