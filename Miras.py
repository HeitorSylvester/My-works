# esse codigo não está completo pois era uma explicação para um amigo
#decotificar 6550126 MMR
#6 = F 
#5 = E 
#50 = L
#1 = I 
# 26 = Z
# MM = 2000
# R = 18

dictionary_numbers = {  # Aplicação de dicionario
'6' : 'F',             
'5' : 'E',              # uso de ":" para separar chaves e valores
'50' : 'L',
'1' : 'I',
'MM' : '2000',
'R' : '18'
}
codified_message = "6550126 MMR" #Entrada da mensagem "6550126 MMR"
separated = list(codified_message) # saida ----> ['6', '5', '5', '0', '1', '2', '6', ' ', 'M', 'M', 'R']
 #transformando a mensagem em vetor usando list,
#não sei se é permitido, mas caso sim, poderia fazer uma matriz ou vetor para comparar cada posição 
# para fazer o retorno não direto do dicionario poderia usar ".get" mas tbm não sei se permite ae poderia fazer
# exemplo 
# primeira_letra = dictionary_numbers.get('6') saida ----> F, entendeu mn?, to cansado pra terminar o codigo :P
#