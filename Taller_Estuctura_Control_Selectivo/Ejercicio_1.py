Dinero=float(input("Ingrese la cantidad que tiene de inversión en el banco: "))
interes=float(input("Ingrese el porcentaje del interes: "))
interes=interes/100
Din_t=Dinero*interes
if ((Din_t)<=100000):
    print("Los intereses no sobrepasan los 100.000 COP")
else:
    print("El dinero total en su cuenta es de:",Din_t+Dinero)

