x=0
prom=0
w=0
h=0
m=0
mn=0
na=0
while True:
    x+=1
    licor=input("¿Consume Licor?: ")
    if(licor=="NO" or licor=="no" or licor=="No"):
        break
    lp=int(input("Cual es su licor favorito: \n1. Aguardiente\n2. Ron\n3. Cerveza\n4. Tequila\n5. Whisky\n6. Otro: "))
    if(lp==0):
        break
    if(lp==5):
        w+=1
    Edad=int(input("Edad: "))
    Sexo=input("Sexo: ")
    if(Sexo=="Hombre" or Sexo=="hombre"):
        h+=1
    if(Sexo=="Mujer" or Sexo=="mujer"):
        m+=1
    
    prom+=(Edad/x)
    porcw=((w*100)/x)
    if(Edad<18 and (Sexo=="Mujer" or Sexo=="mujer")):
        mn+=1
    if(lp!=1 and 20<=Edad<=25 and (Sexo=="Hombre" or Sexo=="hombre")):
        na+=1


print("Numero de encuestados:", x)
print("Mujeres menores de edad:",mn)
print("Hombres que no toman Guaro de 20 a 25 años:",na)
print("El promedio de la edad es:",prom)
print("El porcentaje de personas que beben whisky:",porcw)
