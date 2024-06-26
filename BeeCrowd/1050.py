entrance = int(input)
ddd = [61, 71, 11, 21, 32, 19, 27, 31]
i = 0 
j = 0
while 1 > i:
    if ddd[j] == entrance:
        print ("Brasilia")
    else:
        j+=1
    if ddd[j] == entrance:
        print ("Salvador")
    else:
        j+=1
    if ddd[j] == entrance:
        print ("Sao Paulo")
    i+=1