a=0
g=0
d=0
while True:
    numeros=int(input(""))
    if(numeros==4):
        break
    if(numeros==1):
        a=a+1
    if(numeros==2):
        g=g+1
    if(numeros==3):
        d=d+1
print("MUITO OBRIGADO")
print(f"Alcool: {a}\nGasolina: {g}\nDiesel: {d}")