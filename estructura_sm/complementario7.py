#Calculo de raíces relaes
print("Dada la forma de una ecuación cuadrática: ax^2 + bx + c, con a,b,c y a!=0 Ingrese los siguientes valores:")
a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
d = b**2 - 4*a*c # bhaskara: -b +- ((b^2 - 4.a.c )^1/2)/2.a 
raiz1 = (-1* b + ((b**2 - 4*a*c )**1/2)/2*a)
raiz2 = (b + ((b**2 - 4*a*c )**1/2)/2*a)
if a == 0 :
    print("Math Error")
else :
    if d>0 : 
        print(raiz1) 
        print(raiz2) 