from posixpath import split
datos=input()
(a,b)=datos.split(" ")
a=int(a)
b=int(b)

while(a!=0 and b!=0):
    c=a*b
    print(c)
    datos=input()
    (a,b)=datos.split(" ")
    a=int(a)
    b=int(b)

    
