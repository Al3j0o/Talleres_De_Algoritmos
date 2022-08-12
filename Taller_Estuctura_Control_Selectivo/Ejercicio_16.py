import math
a=float(input("Ingrese A: "))
b=float(input("Ingrese B: "))
c=float(input("Ingrese C: "))
x=float()
form=(a*(x**2))+(b*x)+c 
d=(b**2)-(4*a*c)    
if(d==0):
    x1=x2=-b/(2*a)
    print(x1)
elif(d>0):
    x1=(-b+(math.sqrt((b*2)-(4*a*c))))/(2*a)
    x2=(-b-(math.sqrt((b*2)-(4*a*c))))/(2*a)
    print(x1)
    print(x2)

elif(d<0):
    print("No tiene solución en los reales")