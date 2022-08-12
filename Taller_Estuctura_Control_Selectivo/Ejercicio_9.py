compra=float(input("Ingrese el valor de la compra: "))
if(compra<50000):
    print("No hay descuento")
elif(compra>=50000 and compra<100000):
    print("El total de la compra es:",compra+(compra*0.05))
elif(compra>=100000 and compra<700000):
    print("El total de la compra es:",compra+(compra*0.11))
elif(compra>=700000 and compra<1500000):
    print("El total de la compra es:",compra+(compra*0.18))
elif(compra>=1500000):
    print("El total de la compra es:",compra+(compra*0.25))
    