compra=float(input("Ingrese el valor de la compra: "))
if(compra>5000000):
    inversion=compra*0.55
    prestamo=compra*0.30
    resto=compra-(inversion+prestamo)
    print("Su inversion es:",inversion)
    print("El monto a pagar por el prestamo es: ")
    print("No hay intereses")
elif(compra<=5000000):
    inversion=compra*0.7
    pago=compra*0.3
    interes=pago*0.2
    print("La inversion es de:",inversion)
    print("Debe pagar del prestamo:",pago)
    print("Los intereses son de:",interes)
    

