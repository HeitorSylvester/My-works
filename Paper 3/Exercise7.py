q = int (input()) #quantidade de algarismos a serem digitados 
i = 0 #formação do while 
impar = 0 #auxiliar 
par = 0 #auxiliar 
while q > i :
    a = int (input ()) #valores que vão entrar
    if a % 2 == 0 :
        par = a + par
    else :
        impar = a + impar
    i = i + 1
print ("somas par: " + str (par),"///// somas impares: " + str (impar))