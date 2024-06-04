#Escreva um programa que leia um número e informe se ele é divisível por 10,
#por 5 ou por 2 ou se não é divisível por nenhum deles

print ("digite um numero abaixo")
a = int (input ()) #escrever numero abaixo :thumbs_up:

b = a % 10 #dividir os valores e apenas coletar o resto para sim verificar se é divisivel por tais valores
c = a % 5  
d = a % 2

if b == 0 : 
    print ("eu sou divisivel por 10")
elif c == 0 :
    print ("eu sou divisivel por 5")
elif d == 0 :
    print ("eu sou divisivel por 2") 
else :
    print ("eu não sou divisor de ninguém")

