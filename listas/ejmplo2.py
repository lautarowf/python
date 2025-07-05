suma_temperaturas = 0
media_temperaturas = 0
lista_temperaturas = []
temperaturas_sup_media = 0
cantidad_de_temperaturas = int(input("Ingrese el tamano de la lista: "))
for i in range (cantidad_de_temperaturas):
    temperatura_actual = float(input(f"Ingrese la Temperatura {i+1}: "))
    lista_temperaturas.append(temperatura_actual)
    suma_temperaturas += temperatura_actual
media_temperaturas = suma_temperaturas/cantidad_de_temperaturas
for temperatura in lista_temperaturas:
    if temperatura >= media_temperaturas:
        temperaturas_sup_media += 1
print(media_temperaturas)
print(temperaturas_sup_media)