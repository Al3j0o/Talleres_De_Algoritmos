Sueldo=float(input("Ingrese el sueldo del trabajador: "))
if(Sueldo<900000):
    Sueldo=Sueldo+(Sueldo*0.15)
    print("Su nuevo sueldo es de:", Sueldo)
else: 
    Sueldo=Sueldo+(Sueldo*0.12)
    print("Su nuevo sueldo es de:", Sueldo)