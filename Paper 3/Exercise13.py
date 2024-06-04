val = int (input())
i = 0 
aux = 0 
verifica = True
while val > i :
    digit = int (input())
    if digit >= aux :
        aux = digit
        digit = True 
    else:
        verifica = False
    i += 1 
if verifica == True:
    print ("cresecente")
if verifica == False:
    print ("não cresecente")