#entando descobrir se um dado era viciado, um dono de cassino o lançou n vezes.
#Dados os n resultados dos lançamentos (um por linha), determinar o número de
#ocorrências de cada face.
#Exemplo: se n = 8 e os resultados dos lançamentos são 6, 5, 3, 1, 6, 1, 2, 4, então
#a saída deve ser 2, 1, 1, 1, 1, 2.                     

#6, 5, 4, 3, 2, 1
#2, 1, 1, 1, 1, 2

n = int(input())
vector = []
dice = [6, 5, 4, 3, 2, 1]
print(dice)
i = 0
aux = 0
while n > i:
    dice_launch = int(input())
    vector.append(dice_launch)
    if vector[i] == dice[i]:
        aux = dice[i]
        print (aux)
    
    i+=1