#Tiempo total de viaje 
print("Ingrese el tiempo que tardo en recorrer el primer tramo")
HorasPrimerTramo = int(input("Horas: "))
MinutosPrimerTramo = int(input("Minutos: "))

print("Ingrese el tiempo que tardo en recorrer el segundo tramo")
HorasSegundoTramo = int(input("Horas: "))
MinutosSegundoTramo = int(input("Minutos: "))

TotalMinutos = MinutosPrimerTramo+MinutosSegundoTramo
HorasExtra = TotalMinutos // 60
TotalMinutos = TotalMinutos % 60
TotalHoras = HorasPrimerTramo+HorasSegundoTramo

print("El tiempo total fue de: ",TotalHoras, "Hs y ",TotalMinutos, "Minutos")