#!/usr/bin/python3
aniversarios = {'Maria':'Abril 1',	'Joana':'Dezembro 12','Carol':'Fevereiro 4'}

while	True:
    print('Informe o nome:	(blank	to	quit)')	
    nome = input() 
    if	nome ==	'':
        break
    if	nome in	aniversarios: 
         print( + ' is the birthday of ' + nome)
    else:
       	print('What	is	their	birthday?')
        bday =	input()
        aniversarios[nome] = bday
        print('Aniversario	database atualizado.')