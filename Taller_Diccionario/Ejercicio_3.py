from re import I


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

print(usuarios["iperurena"])

a=input("ingrese su usuario: ")
b=int(input("Ingrese la contraseña: "))
c=0
while (a!=usuarios["iperurena"] and a!=usuarios["aolaizola"] and a!=usuarios["fmuguruza"]):
    c+=1


print(usuarios.keys())
        


