n = int (input ())
i = 0 
posi = 0 
nega = 0 
while n > i :
    cha = int (input ())
    if cha < 0 :
        nega = nega + 1
    if cha >= 0 :
        posi = posi + 1
    i = i + 1
print ("valores positivos " + str (posi) + "   valores negativos " + str (nega))