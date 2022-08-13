hemo=float(input("Ingrese los niveles de hemoglobina: "))
sex=(input("Ingrese su sexo: "))
ano=int(input("Ingrese los años que tiene: "))
meses=int(input("Ingrese los meses que tiene: "))
if(ano==0 and meses<=1 ):
    if((hemo>=13) and (hemo<=26)):
        print("niveles normales de hemoglobina")
    elif((hemo<=13) and (hemo>=26)):
        print("tiene anemia") 
if(ano==0 and meses>1 and meses<=6 ):
    if((hemo>=10) and (hemo<=18)):
        print("niveles normales de hemoglobina")
    elif((hemo<=10) and (hemo>=18)):
        print("tiene anemia") 
if(ano==0 and meses<6 and hemo<=12):
    if((hemo>=11) and (hemo<=15)):
        print("niveles normales de hemoglobina")
    elif((hemo<=11) and (hemo>=15)):
        print("tiene anemia") 
if(ano>1 and ano<=5 ):
    if((hemo>=11.5) and (hemo<=15)):
        print("niveles normales de hemoglobina")
    elif((hemo<=11.5) and (hemo>=15)):
        print("tiene anemia") 
if(ano>5 and ano<=10):
    if((hemo>=12.6) and (hemo<=15.5)):
        print("niveles normales de hemoglobina")
    elif((hemo<=12.6) and (hemo>=15.5)):
        print("tiene anemia") 
if(ano>10 and ano<=15 ):
    if((hemo>=13) and (hemo<=15.5)):
        print("niveles normales de hemoglobina")
    elif((hemo<=13) and (hemo>=15.5)):
        print("tiene anemia")  
if(ano>15 and sex=="Hombre" ):
    if((hemo>=12) and (hemo<=16)):
        print("niveles normales de hemoglobina")
    elif((hemo<=12) and (hemo>=16)):
        print("tiene anemia")
if(ano>15 and sex=="Mujer" ):
    if((hemo>=14) and (hemo<=18)):
        print("niveles normales de hemoglobina")
    elif((hemo<=14) and (hemo>=18)):
        print("tiene anemia")        
    


