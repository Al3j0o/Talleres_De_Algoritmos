sueldo=float(input("Ingrese su sueldo base: "))
ven1=float(input("Ingrese el valor de la primera venta: "))
ven2=float(input("Ingrese el valor de la segunda venta: "))
ven3=float(input("Ingrese el valor de la tercera venta: "))
com1=ven1*0.1
com2=ven2*0.1
com3=ven3*0.1
print("El ingreso solo por comisiones es:", com1+com2+com3)
print("El ingreso total es:", com1+com2+com3+sueldo)
