i = 0 
aux = 1
auf = 0
digit = int (input("digite abaixo uma sequencia de numeros!:")) #2 3 6 6 7
while digit != 0 :
    aux = digit % 10
    digit = int(digit/10)     
    auf = digit % 10
    if auf == aux :
        das = True
        # break usando break da certo mas não pode usar
    elif auf != aux:
        das = False
#    print (das, auf, aux)
    if das == True :
        print ("Há sim consecutivos iguais, são eles: \n"   + str (aux) + str (auf))
    else :
       das = das
    i += 1
