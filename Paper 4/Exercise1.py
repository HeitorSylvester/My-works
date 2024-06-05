entrance = int(input()) #4
i = 0
vector=[]
while entrance > i: # 4 > i  0 1 2 3 
    numbers = int(input()) # 3 5 9 7
    vector.append(numbers)
    i += 1
i -= 1
while i >= 0:
    print(vector[i], end=" ")
    i-=1