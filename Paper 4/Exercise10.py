values = input().split()
print (values)
i = 0
aux = []
appender = 0
j = 0
while len(values) > i:
    if values[i] == values[j-1]:
        appender = values[i]
        aux.append(appender)
    i+=1
    j+=1
print (aux)