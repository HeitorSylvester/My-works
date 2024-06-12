gabarito = input().split() #vetor gabarito
alunos = int(input())
i=0
ponta = 0
vetor=[]
while alunos > i:
    respostas = input()
    vetor.append(respostas) #vetor respostas
    print(vetor[ponta])
    ponta+=1
    i+=1
# Não terminado