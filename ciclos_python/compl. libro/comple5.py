CONTRASENA = "alumno"
RESPUESTA = "Salem"

intentos_contrasena = 0
intentos_respuesta = 0
acceso_concedido = False

# Primer intento: contraseña
while intentos_contrasena < 3:
    posible_contrasena = input("Ingrese su contraseña: ")
    intentos_contrasena += 1
    if posible_contrasena == CONTRASENA:
        print("Inicio de sesión exitoso.")
        acceso_concedido = True
        break
    else:
        print("Contraseña incorrecta.")

# Si no logró ingresar la contraseña, se pasa a la pregunta de seguridad
if not acceso_concedido:
    print("\nAgotó los intentos de contraseña.")
    print("Debe responder una pregunta de seguridad para desbloquear.")
    
    while intentos_respuesta < 2:
        posible_respuesta = input("¿Cuál es el nombre de tu mascota? ")
        intentos_respuesta += 1
        if posible_respuesta == RESPUESTA:
            print("Desbloqueo exitoso. Inicio de sesión permitido.")
            acceso_concedido = True
            break
        else:
            print("Respuesta incorrecta.")

# Si falla también la segunda validación
if not acceso_concedido:
    print("\nSistema bloqueado. Contacte al administrador.")
