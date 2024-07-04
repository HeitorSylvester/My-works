times = int(input()) #qtd de valores pro vetor # 5
vector = []
i = 0 
j = 0  #5
aux = times - 1
while times > i: #aplicação dos valores no vetor
    value = int(input())
    vector.append(value)
    i+=1
# 5, 3, 2, 7, 9
i = 0 
while times > i: # verificação do menor valor
    if vector[j] > vector[i]:
        aux = vector[i]
        j+=1
    i+=1
print ("O menor valor é  " + str (aux))