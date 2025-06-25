primer_numero = 0
segundo_numero = 1
while segundo_numero <= 10000:
    sumaF= primer_numero+segundo_numero
    primer_numero = sumaF
    segundo_numero =sumaF - segundo_numero
    print(sumaF)