def mdc (a, b): #a = 42 b = 30 
    i = 0
    while a and b != i :
        div_1 = a % b # equals 12 
        div_2 = div_1 % b
        print (div_2)
        div_3 = div_1 % div_2 
        i += 1
    print (div_3)

first = int (input())
second = int (input())
gtx = mdc (first, second)