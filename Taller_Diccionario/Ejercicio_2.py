Diccionario= {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
lista=[]
for i in Diccionario:
    if (not(Diccionario[i] in lista)):
        lista.append(Diccionario[i])
    #print(list(set(lista)))
print(lista)