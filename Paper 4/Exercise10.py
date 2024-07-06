values = input().split()
i = 0
aux = []
appender = 0
j = 0
while len(values) > i:
    if values[i] == values[j-1]: 
        aux.append(values[i])
#    if values == values [j]:
#        aux.append (values[i])
    i+=1
    j+=1
print (aux)