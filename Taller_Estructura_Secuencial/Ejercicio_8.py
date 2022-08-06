from cmath import sqrt
import math
a=float(input("Ingrese el primer lado del triangulo: "))
b=float(input("Ingrese el segundo lado del triangulo: "))
c=float(input("Ingrese el tercer lado del triangulo: "))
sp=(a+b+c)/2
area=sqrt(sp*(sp-a)*(sp-b)*(sp-c))
print("El area es:", area)
