precf=float(input("Ingrese el precio final pagado por el producto: "))
pvp=float(input("Ingrese el valor de venta al publico: "))
Desc=100-((100*precf)/pvp)
print("El porcentaje de descuento es de:",Desc," %")