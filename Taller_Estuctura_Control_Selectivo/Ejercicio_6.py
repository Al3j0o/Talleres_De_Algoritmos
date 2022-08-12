a=int(input("Ingrese A: "))
b=int(input("Ingrese B: "))
c=int(input("Ingrese C: "))
d=int(input("Ingrese D: "))
x=(f"{a}{b}")
z=(f"{c}{d}")
n=(f"{a}{b}{c}{d}")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
n=int(n)
x=int(x)
z=int(z)
if(z>50 and b==9):
    n=(f"{a+1}{0}{0}{0}")
    print(n)
elif(z<=50):
    n=(f"{a}{b}{0}{0}")
    print(n)
elif(z>50):
    n=(f"{a}{b+1}{0}{0}")
    print(n)

