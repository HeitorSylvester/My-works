n = int (input()) #quantidade de valores para fazer a adição 4
i = 0 #base do while 
aux = 0 
while n > i:
    valores = int (input())# 4 5 2 1
    aux = valores + aux  #armazenamento na aux 
    i = i + 1 
print (aux)