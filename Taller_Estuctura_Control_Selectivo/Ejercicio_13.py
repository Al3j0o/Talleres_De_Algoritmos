from datetime import date
from posixpath import split
today=date.today()
dia_a=today.day
mes_a=today.month
año_a=today.year
Nacim=input("Ingrese su fecha de cumpleaños año/mes/dia: ")
(año,mes,dia)=Nacim.split("/")
año_n=int(año)
mes_n=int(mes)
dia_n=int(dia)
Edad=0

if(mes_n==mes_a):
    if(dia_a>=dia_n):
        Edad=año_a-año_n
    else:
        Edad(año_a-año_n)-1
elif(mes_a>mes_n):
    Edad=año_a-año_n
else:
    Edad=(año_a-año_n)-1

signo=""
if((22<=dia_n<31 and mes_n==11) or (1<dia_n<=21 and mes_n==12)):
    signo="Sagitario"
elif((22<=dia_n<31 and mes_n==12) or (1<dia_n<=20 and mes_n==1)):
    digno="Capricornio"
elif((21<=dia_n<31 and mes_n==1) or (1<dia_n<=19 and mes_n==2)):
    signo="Acuario"
elif((20<=dia_n<28 and mes_n==2) or (1<dia_n<=19 and mes_n==3)):
    signo="Piscis"
elif((21<=dia_n<30 and mes_n==3) or (1<dia_n<=20 and mes_n==4)):
    signo="Aries"
elif((21<=dia_n<30 and mes_n==4) or (1<dia_n<=21 and mes_n==5)):
    signo="Tauro"
elif((22<=dia_n<30 and mes_n==5) or (1<dia_n<=21 and mes_n==6)):
    signo="Géminis"
elif((22<=dia_n<30 and mes_n==6) or (1<dia_n<=22 and mes_n==7)):
    signo="Cáncer"
elif((22<=dia_n<23 and mes_n==7) or (1<dia_n<=23 and mes_n==8)):
    signo="Leo"
elif((24<=dia_n<30 and mes_n==8) or (1<dia_n<=22 and mes_n==9)):
    signo="Virgo"
elif((23<=dia_n<30 and mes_n==9) or (1<dia_n<=22 and mes_n==10)):
    signo="Libra"
elif((23<=dia_n<30 and mes_n==10) or (1<dia_n<=21 and mes_n==11)):
    signo="Esorpio"

print(Edad)
print(signo)