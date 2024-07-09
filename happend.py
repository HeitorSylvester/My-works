value = input().split()
i = 0
counter = 0
result = 0
while len (value) > i:
    counter = 0
    result = 0
    if value == value[i]:
        counter +=1
        result = value[i]
    i+=1
    print (counter, result)
