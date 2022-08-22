n=int(input("Ingrese la cantidad de estudiantes: "))
cm=float(input("Cual es la calficacion mas alta que se puede conseguir: "))
x=1
notal=-1
nota2=cm+1
Pun2=0
while(x<=n):
    x+=1
    Nom=input("Ingrese su nombre: ")
    Pun=float(input("Ingrese su puntaje: "))

    Pun2+=Pun
    prom=Pun2/n
    if(Pun>notal):
        notal=Pun
    if(Pun<nota2):
        nota2=Pun
    if(Pun<prom):
        porcdeb=(prom*n)/100
    if(Pun>prom):
        porcsup=(prom*n)/100
    


print("La nota mas alta es:",notal)
print("La nota mas bajas es:",nota2)
print("Porcentaje superior al promedio:",porcsup)
print("porcentaje inferior al promedio:",porcdeb)
print("El promedio es:",prom)


