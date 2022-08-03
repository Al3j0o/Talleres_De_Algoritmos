Algoritmo Ejercicio_18
	Escribir "Ingrese su nombre: "
	Leer Nombre
	Escribir "Ingrese su primer apellido: "
	Leer Apellido1
	Escribir "Ingrese su segundo apellido: "
	Leer Apellido2
	NOM<-Mayusculas(Nombre)
	APELLIDO1<-Mayusculas(Apellido1)
	APELLIDO2<-Mayusculas(Apellido2)
	NOM1<-Subcadena(NOM,0,1)
	Ape1<-Subcadena(APELLIDO1,0,1)
	Ape2<-Subcadena(APELLIDO2,0,1)
	Iniciales<-Concatenar(NOM1,Ape1)
	INICI<-Concatenar(Iniciales,Ape2)
	Escribir INICI
FinAlgoritmo
