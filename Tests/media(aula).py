#VETOR E MATRIZES 
#quantidade de alunos
n= int (input())
i=0
soma = 0 
notas=[] # <--- Vetor 
while i < n:
    nota = float(input())
    notas.append(nota) #<--- concatenar (metodo)
    
    #somar o total das notas 
    soma = soma + soma 
    i+=1
media = soma/n 
i=0
contador = 0
while i < n:
    if notas[i]>media: #<---- literalmente ponteiro em uma reta mostrando valores
        contador +=1
    i +=1
print ("media"+str(media))
print("há" + str (contador)+"alunos acima da media ")

#*****************#

#def troca_primitiva (x,y):
#    aux = x 
#    x = y 
#    y = aux
#
#def troca_vetor(x,pos1,pos2):
#    aux = x [pos1]
#    x[pos1]=x[pos2]
#    x[pos2]=aux
#
#a=10
#b=20
#print ("******",a)
#print ("*******",b)
#troca_primitiva(a,b)
#print ("*******",a)
#print ("*******",b)
#c=[]
#c.append(10)
#c.append(20)
#print (c[0])
#print (c[1])
#troca_vetor(c,0,1)
#print (c[0])
#print (c[1])