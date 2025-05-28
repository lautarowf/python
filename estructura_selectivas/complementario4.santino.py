print("--------------------------------------------------------------")
print("Ejercicio: DETERMINAR DIA SIGUIENTE 2")
print("--------------------------------------------------------------")

print("Ingrese la fecha de hoy: ")
Dia=int(input("Dia: "))
Mes=int(input("Mes: "))
Año=int(input("Año: "))


if Dia<30 and Mes==4 or Mes == 6 or Mes == 9 or Mes == 11:
    DiaFinal=Dia+1
    print("Mañana va a ser: ",DiaFinal,Mes,Año,)
else:
    if Dia==30 and Mes==4 or Mes == 6 or Mes == 9 or Mes == 11:
        DiaFinal=1
        MesFinal=Mes+1
        print("Mañana va a ser: ",DiaFinal,MesFinal,Año,)
    else:
        if ((Dia<31) and (Mes== 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12)):
            DiaFinal=Dia+1
            print("Mañana va a ser: ",DiaFinal,Mes,Año,)
        else:
            if((Dia==31)and (Mes==1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10)) :
                DiaFinal=1
                MesFinal=Mes+1
                print("Mañana va a ser: ",DiaFinal,MesFinal,Año,)
            else:
                if ((Dia<29)  and ((Año%4==0) or (Año%400==0) and (Año%100!=0)) and (Mes==2)):
                    DiaFinal=Dia+1
                    print("Mañana va a ser: ",DiaFinal,Mes,Año,)
                else:
                    if ((Dia==29) and ((Año%4==0) or (Año%400==0) and (Año%100!=0)) and (Mes==2)):
                        DiaFinal=1
                        MesFinal=Mes+1
                        print("Mañana va a ser: ",DiaFinal,MesFinal,Año,)
                    else:
#                        if ((Dia<28) and ((Año%4!=0) or (Año%400!=0) and (Año%100==0)) and (Mes==2)):
#                            DiaFinal=Dia+1
#                            print("Mañana va a ser: ",DiaFinal,Mes,Año,)
#                        else:
#                            if ((Dia==28) and ((Año%4!=0) or (Año%400!=0) and (Año%100==0)) and (Mes==2)):
#                                DiaFinal=1
#                                MesFinal=Mes+1
#                               print("Mañana va a ser: ",DiaFinal,MesFinal,Año,)
#                            else:
                                if Dia==31 and Mes==12:
                                    DiaFinal=1
                                    MesFinal=1
                                    AñoFinal=Año+1
                                    print("Mañana va a ser: ",DiaFinal,MesFinal,AñoFinal,)