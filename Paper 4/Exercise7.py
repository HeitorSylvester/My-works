times = int(input()) #qtd de valores pro vetor # 5
vector = []
i = 0 
handy = 0
handy_1 = 0
j = 0  #5
aux = times - 1
while times > i: #aplicação dos valores no vetor
    value = int(input())
    vector.append(value)
    i+=1
# 5, 3, 2, 7, 9
i = 0 
while times > i: # verificação do menor valor 
    if vector [i-1] > vector [i]:
        handy_1 = [i-1]
    aux -=1
    i+=1
print (handy_1)

#UNFINISHED CODE