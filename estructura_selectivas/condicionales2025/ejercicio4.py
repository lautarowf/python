#Cajero automatico basico
saldo = float(input("Ingrese su saldo: "))
monto_a_retirar = float(input("Ingrese cuanto desea retirar: "))
if monto_a_retirar <= saldo:
    nuevo_saldo = saldo - monto_a_retirar
    print("Su saldo actual es: $", nuevo_saldo)
else:
    print("Fondos insuficientes")    