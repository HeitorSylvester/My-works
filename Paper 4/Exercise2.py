n=int(input()) #6 dias , médias de temeperaturas e quais foram as maiores
i=0     
list=[] 
alpha=0
beta=0
vector=[]
while n > i:
    temps=int(input()) #3,2,1=6
    vector.append(temps) #VETOR SALVA MMAMAMAMAM
    alpha=temps+alpha
    beta+=temps
    i+=1
i-=1
i=0
alpha=[]
beta=round(beta/n,2) #24.5
while n > i:
    vector[i]
    if vector[i] > beta :
        alpha.append(vector[i]) #<----- importante
    i+=1
print(beta,alpha)