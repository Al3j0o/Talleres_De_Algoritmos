nota1=float(input("Ingrese la primera nota del parcial: "))
nota2=float(input("Ingrese la segunda nota del parcial: "))
nota3=float(input("Ingrese la tercera nota del parcial: "))
notaExa=float(input("Ingrese la nota del examen final: "))
notaTra=float(input("Ingrese la nota del trabajo final: "))
PromParc=(nota1+nota2+nota3)/3
print("La nota final es:", (PromParc*0.55)+(notaExa*0.30)+(notaTra*0.15))