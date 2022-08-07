Nom=str(input("Ingrese su nombre: "))
Hij=int(input("Ingrese el numero de hijos que tiene: "))
Hnorm=int(input("Ingrese el numero de horas trabajadas: "))
Pnorm=float(input("Ingrese el pago de una hora normal: "))
hext=int(input("INgrese el numero de horas extras trabajadas: "))
Hext=Hnorm+(Hnorm*0.25)
sueldo=(Hnorm*Pnorm)
Asip=Hij*173000
Deduccion=(sueldo*0.02)-(sueldo*0.05)-(sueldo*0.07)
sueldoT=sueldo-Deduccion+Asip+250000+180000

print("Las deducciones son de:",Deduccion)
print("Las asignaciones son de:",Hext+Asip+250000+180000)
print("el sueldo total es de:",sueldoT)


