Km=float(input("Ingrese la cantidad de kilometros recorridos: "))
if(Km<300):
    print("Cancele 50.000 COP")
if(Km>300):
    if(Km<1000):
        cobro=70000
        exce=(Km-300)*3000
        cobro_t=cobro+exce
        print("Cancela",cobro_t,"COP")
    elif(Km>1000):
        cobro=150000
        exce=(Km-1000)*9000
        cobro_t=cobro+exce
        print("Cancele",cobro_t,"COP")
