print("Calcula el interes")
C = -1
I = 0
M = 0
while (C>0) or (I<=0) or (I>=100) or (M<=0):
    C = int(input("Capital: "))
    I = int(input("Interes: "))
    M = int(input("Tiempo en años: "))
for i in range(M):
    C = C*(1+I/100)
print("Tienes", C, "soles") 