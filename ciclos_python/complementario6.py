CONTRASENA = "lennon"
intentos = 0
while intentos <3:
    posible_contrasena = str(input("Ingrese su contrasen: "))
    if posible_contrasena == CONTRASENA:
        print("Se ha iniciado sesion")
        break
    else:
        print("Contrasena incorrecta")
    intentos += 1
if intentos == 3:
    print("Usuario bloqueado")    