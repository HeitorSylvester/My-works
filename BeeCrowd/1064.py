i = 0 
auxiliary = 0
counter = 0
while 6 > i:
    value = float(input())
    if value < -0.1:
        value = 0

    elif value > 0:
        auxiliary += value
        counter +=1
    i+=1
sum = auxiliary / counter
print (counter, "valores positivos")
print ("%0.1f"%sum)
