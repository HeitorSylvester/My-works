q = int (input ()) #quantidade de algarismos a ser escrito
i = 0 #criação da estrutura de repetição (while)
aux = 0 #auxiliar para armazenar os algarismos escritos 
while q > i :
    num = int (input ()) #algarismos
    if num < 0 :
        num = 0
    aux = num + aux
    i = i + 1
print (aux) 
    