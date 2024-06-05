def le_numeros(n):
    numeros =[]
    i=0
    while i<n:
        numero=int(input())
        if numero>=0 and numero<=36:
            numeros.append(numero)
            i+=1
        else:
            print ("não fui mlk escreve 0 a 36")    
    
    return numeros 

n=int(input())
valores=le_numeros(n)

