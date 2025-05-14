#Costo total del viaje
recorridoEnKilometros = 250
consumo_combusible = 0.05 #5 Lt cada 100KM
precio_combustible = 1000 #Pesos

consumo_viaje = recorridoEnKilometros*consumo_combusible*precio_combustible

print("El costo total es: $", consumo_viaje)