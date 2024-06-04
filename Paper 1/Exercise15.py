a1 = "Digite sua altura abaixo: \n"
print (a1)
altura = input ()
altura2 = float (altura)
homens = round ( (72.7 *altura2) - 58,2)
mulher = round ( (62.1 * altura2) - 44.7,2)
print ("O peso ideal caso seja mulher é de: \n" + str (mulher) + " Kilos")
print ("O peso ideal caso seja homem é de \n" + str (homens) + " Kilos")