sueldo=float(input("Ingrese el salario bruto de los trabajadores: "))
venta=float(input("Ingrese el valor de las ventas totales: "))
depa1=float(input("Ingrese el dinero ganado en el departamento 1: "))
depa2=float(input("Ingrese el dinero ganado en el departamento 2: "))
depa3=float(input("Ingrese el dinero ganado en el departamento 3: "))

if(depa1>venta*0.33):
    sueldo=sueldo+(sueldo*0.20)
    print("Su sueldo total es de:",sueldo)
if(depa2>venta*0.33):
    sueldo=sueldo+(sueldo*0.20)
    print("Su sueldo total es de:",sueldo)
if(depa3>venta*0.33):
    sueldo=sueldo+(sueldo*0.20)
    print("Su sueldo total es de:",sueldo)
else:
    print("No hay aumento de sueldo")