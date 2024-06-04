a =int(input()) # entrada 4
b = 0
c = 0
d = 0
final = "" # soma de strings com espaço
while a > b :
    soma=c+d
    aux=c
    c=d
    d=aux+d
    if b==0:
        c=1
        final=str(soma)
    else:
        final=final+" "+str(soma)

    b = b + 1 #saida 0 1 1 2 3  
print (final)