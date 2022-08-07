mat1=float(input("Ingrese la primera nota de matematicas: "))
mat2=float(input("Ingrese la segunda nota de matematicas: "))
mat3=float(input("Ingrese la tercera nota de matematicas: "))
Exma=float(input("Ingrese la nota del examen: "))

fis1=float(input("Ingrese la primera nota de fisica: "))
fis2=float(input("Ingrese la segunda nota de fisica: "))
Exfi=float(input("Ingrese la nota del examen: "))

qui1=float(input("Ingrese la primera nota de quimica: "))
qui2=float(input("Ingrese la segunda nota de quimica: "))
qui3=float(input("Ingrese la tercera nota de quimica: "))
Exqui=float(input("Ingrese la nota del examen: "))

proma=(((mat1+mat2+mat3)/3)*0.1)+(Exma*0.9)
promfi=(((fis1+fis2)/2)*0.2)+(Exfi*0.8)
promqui=(((qui1+qui2+qui3)/3)*0.15)+(Exqui*0.85)

print("Su nota final en matematica es:",proma)
print("Su nota final en fisica es:",promfi)
print("Su nota final en quimica es:",promqui)

