n = int (input ())
i = 0 
par = 0 
impar = 0 
while n > i :
    val = int (input ())
    if val % 2 == 0:
        par = par + 1
    else :
        impar = impar + 1
    i = i + 1
print ("valores pares " + str (par) + "  valores impares " + str (impar))