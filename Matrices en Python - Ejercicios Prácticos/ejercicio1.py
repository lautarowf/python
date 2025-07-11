numero_de_pacientes = int(input("Ingrese la cantidad de pacientes: "))
matriz_pacientes = []
valor_de_coberturta = 5000
suma_costos = 0
pacientes_costo_exedido = []
for pacientes in range(numero_de_pacientes):
    datos = []
    paciente_nombre = str(input("Ingrese el nombre del paciente: "))
    paciente_diagnostico = str(input("Ingrese el diagnostico del paciente: "))
    paciente_costo = float(input("Ingrese el costo del tratamiento: "))
    suma_costos += paciente_costo
    datos.append([paciente_nombre, paciente_diagnostico, paciente_costo])
    matriz_pacientes.append(datos)
    if paciente_costo > valor_de_coberturta:
        pacientes_costo_exedido.append(paciente_nombre)
for datos in matriz_pacientes:
    print(datos)
print(f"Pacientes que han exedido el valor de cobertura: {pacientes_costo_exedido}")
print(f"Costo total: ${suma_costos}")