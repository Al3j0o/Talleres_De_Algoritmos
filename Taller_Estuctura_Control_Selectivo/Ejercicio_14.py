lectura_a=float(input("Ingrese los Kwh de la lectura del mes anterior: "))
lectura_b=float(input("Ingrese los Kwh de la lectura de este mes: "))
Kwh=lectura_a-lectura_b
if(Kwh>0 and Kwh<=100):
    Kwh=Kwh*4600
    print("debe pagar:",Kwh)
elif(Kwh>100 and Kwh<=300):
    Kwh=Kwh*80000
    print("Debe pagar:",Kwh)
elif(Kwh>300 and Kwh<=500):
    Kwh=Kwh*100000
    print("Debe pagar:",Kwh)
elif (Kwh>500):
    Kwh=Kwh*120000
    print("Debe pagar:",Kwh)
    