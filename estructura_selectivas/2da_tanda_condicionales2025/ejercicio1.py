#Validacion de temperatura corporal
temperatura = float(input("Ingrese la temperatura corporal (en C°): "))
if temperatura < 36 :
    print("Hipotermia")
elif temperatura < 37.5 :
    print("Normal") 
elif temperatura >= 37.5 :
    print("Fiebre")    