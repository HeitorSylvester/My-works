#entando descobrir se um dado era viciado, um dono de cassino o lançou n vezes.
#Dados os n resultados dos lançamentos (um por linha), determinar o número de
#ocorrências de cada face.
#Exemplo: se n = 8 e os resultados dos lançamentos são 6, 5, 3, 1, 6, 1, 2, 4, então
#a saída deve ser 2, 1, 1, 1, 1, 2.                     

#6, 5, 4, 3, 2, 1
#2, 1, 1, 1, 1, 2

dice = int (input("Digite a qtd de lançamentos:  "))
i=0
vector = []
auxiliary = []
while dice > i:
    dice_values = int (input())
    vector.append(dice_values)
    i+=1
    while len vector > i:
        
print (vector)