from multiprocessing.sharedctypes import Value


print("se esta calificando sobre 50")
# estudiantes={

#     "1":{
#         "nombre1":input("Ingrese el nombre del primer estudiante: "),
#         "nota":int(input("Ingrese la nota del estudiante 1: "))
#     },
#     "2":{
#         "nombre":input("Ingrese el nombre del estudiante 2: "),
#         "nota":int(input("Ingrese la nota del estudiante 2:"))
#     },
#     "3":{
#         "nombre":input("Ingrese el nombre del estudiante 3: "),
#         "nota":int(input("Ingrese la nota del estudiante 3:"))
#     },
#     "4":{
#         "nombre":input("Ingrese el nombre del estudiante 4: "),
#         "nota":int(input("Ingrese la nota del estudiante 4:"))
#     },
#     "5":{
#         "nombre":input("Ingrese el nombre del estudiante 5: "),
#         "nota":int(input("Ingrese la nota del estudiante 5:"))
#     },
#     "6":{
#         "nombre":input("Ingrese el nombre del estudiante 6: "),
#         "nota":int(input("Ingrese la nota del estudiante 6:"))
#     },
#     "7":{
#         "nombre":input("Ingrese el nombre del estudiante 7: "),
#         "nota":int(input("Ingrese la nota del estudiante 7:"))
#     },
#     "8":{
#         "nombre":input("Ingrese el nombre del estudiante 8: "),
#         "nota":int(input("Ingrese la nota del estudiante 8: "))
#     },
#     "9":{
#         "nombre":input("Ingrese el nombre del estudiante 9: "),
#         "nota":int(input("Ingrese la nota del estudiante 9: "))
#     },
#     "10":{
#         "nombre":input("Ingrese el nombre del estudiante 10: "),
#         "nota":int(input("Ingrese la nota del estudiante 10: "))
#     }

# }
prueba={
    "1":{
        "nombre":"carlos",
        "nota":34

    },
    "2":{
        "nombre":"diana",
        "nota":25
    },
    "3":{
        "nombre":"jorge",
        "nota":29
    }


}
lista=[]
aux=[]
nombre=""
nota=0
tupla=(nombre,nota)
listax=prueba.items()
for x,y in listax:
    for z in y.values() :
        aux.append(z)
        if(z==str()):
            z=nombre
        if(z==int()):
            z=nota
        aux.append(tupla)
        
print(aux)


        
