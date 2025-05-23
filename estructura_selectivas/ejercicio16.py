#ordenar de mayor a menor
print("Ingrese 3 numeros para ordenarlos de mayor a menor: ")
numero_a = int(input())
numero_b = int(input())
numero_c = int(input())
if numero_a > numero_b :
    if numero_a > numero_c :
        if numero_b > numero_c :
            print(numero_a, numero_b, numero_c)
        else :
            print(numero_a, numero_c, numero_b)
    else : 
        print(numero_c, numero_a, numero_b)
else :
    if numero_b > numero_a :
        if numero_b > numero_c:
            if numero_a > numero_c:
                print(numero_b, numero_a, numero_c)
            else:
                print(numero_b, numero_c, numero_a)
        else :
            print(numero_c, numero_b, numero_a)            