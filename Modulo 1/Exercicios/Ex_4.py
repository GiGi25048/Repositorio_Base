# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE
soma= 0
contador = 0
while contador < len(notas):
     nota=float(notas[contador])
     soma= soma+nota
     contador =  contador+1
     media= soma/len(notas)
print(media)




# LOOP FOR

#for nota in notas:
    #n=float(nota)
    #contador= contador+1
    
