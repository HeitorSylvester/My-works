a1 = int (input ("Escreva abaixo, em metros quadrados a área para ser pintada \n")) 
quad =  a1 / 3
gal = quad * 6.95
quad1 = 4.45 * quad #fiz a transformação de 18 litros que valiam 80 reais para que 1 litro vale 4.45 facilitando o calculo (não julga)
quad = round (quad,2) #apesar do uso proibido do "round" eu usei pq mto numero me dá um treco assim como a ","
quad1 = round (quad1,2)
print ("A quantidade de latas será de \n" + str (quad) + " Latas")
print ("Preço final é de: \n" + str  (quad1) + " Reais")