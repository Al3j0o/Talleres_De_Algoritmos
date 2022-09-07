
usuarios = { 
"iperurena": { 
"nombre": "Iñaki", 
"apellido": "Perurena", 
"password": "123123" 
}, 
"fmuguruza": { 
"nombre": "Fermín", 
"apellido": "Muguruza", 
"password": "654321" 
}, 
"aolaizola": { 
"nombre": "Aimar", 
"apellido": "Olaizola", 
"password": "123456" 
} 
} 
listap=[]
listaf=[]
listal=[]

c=0
for i in usuarios["iperurena"].values():
    listap.append(i)
listap[2]=int(listap[2])

    
for x in usuarios["fmuguruza"].values():
    listaf.append(x)
listaf[2]=int(listaf[2])
    
for y in usuarios["aolaizola"].values():
    listal.append(y)
listal[2]=int(listal[2])

user=input("Ingrese el usuario: ")
contra=int(input("Ingrese la contraseña: "))

while(c<3):
    if(user!="iperurana" and user!="fmuguruza" and user!="aolaizola"):
        c+=1
        print("usuario inválido")
        user=input("Ingrese el usuario: ")
        contra=int(input("Ingrese la contraseña: "))
    if(contra!=listaf[2] and contra!=listal[2] and contra!=listap[2]):
        print("Contraseña inválida")
        user=input("Ingrese el usuario: ")
        contra=int(input("Ingrese la contraseña: "))
    elif(user=="iperurana" and contra==listap[2]):
        print(listap[0],listap[1])
        break
    elif(user=="fmuguruza" and contra==listaf[2]):
        print(listaf[0],listaf[1])
        break
    elif(user=="aolaizola" and contra==listal[2]):
        print(listal[0],listal[1])
        break

    

        


