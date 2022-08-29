archivo_edad=open("Archivos/edad.txt","r",encoding="UTF-8")
archivo_escolar=open("Archivos/escolaridad.txt","r",encoding="UTF-8")
archivo_estado=open("Archivos/estado_civil.txt","r",encoding="UTF-8")
archivo_estrato=open("Archivos/estrato.txt","r",encoding="UTF-8")
archivo_sexo=open("Archivos/sexo.txt","r",encoding="UTF-8")
archivo_promedio=open("Archivos/promedio.txt","r",encoding="UTF-8")
archivo_region=open("Archivos/region.txt","r",encoding="UTF-8")
lista=[]


for linea1 in archivo_edad:
    lista.append(int(linea1.strip()))
    for linea2 in archivo_escolar:
        lista.append(linea2.strip())
        for linea3 in archivo_estado:
            lista.append(linea3.strip())
            for linea4 in archivo_estrato:
                lista.append(int(linea4.strip()))
                for linea5 in archivo_sexo:
                    lista.append(linea5.strip())
                    for linea6 in archivo_promedio:
                        lista.append(float(linea6.strip()))
                        for linea7 in archivo_region:
                            lista.append(linea7.strip())       



print(lista)





   

#[(id,edad,escolaridad,estdo_c,estrato,sexo,promedio,region)]