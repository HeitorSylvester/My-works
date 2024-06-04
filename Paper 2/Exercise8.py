#Escreva um programa que leia um número e imprima se ele é igual a 5, a 200, a 400,
# se está no intervalo entre 500 e 1000, ou se ela está fora dos escopos anteriores

print ("digite um valor abaixo")
a = int (input ())

if a == 5 :
        print (" eu sou igual a 5")
elif a == 200 :
        print ("eu sou igual a 200")
elif a == 400 :
        print (" eu sou igual a 400")

elif a > 500 and a < 1000 :
        print ("eu estou no intervalo entre 500 e 1000")
else :
        print ("eu não estou nesse intervalo")