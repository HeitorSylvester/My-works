print ("digite 3 valores abaixo ")
x = int (input ()) #menor numero 
y = int (input ()) #numero mediano 
z = int (input ()) #maior numero

if z < y and z < x : #z é o maior
    if y < x : #y é o segundo maior 
        print (z,y,x)
    elif x < y : # x é o segundo maior
        print (z,x,y)

if y < z and y < x : # y é o maior
    if z < x : #z é o segundo maior
        print (y,z,x)
    elif x < z : # x é o segundo maior
        print (y,x,z)

if x < z and x < y : #x é o maior
    if z < y : #z é o segundo maior
        print (y,z,x)
    elif y < z : # y é o segundo maior
        print (x,y,z)
      