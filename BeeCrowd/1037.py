entrance = float(input()) 

if entrance < 0:
    print ("Fora de intervalo")
elif 0 > entrance or entrance <= 25:
    print ("Intervalo [0,25]")
elif 25 > entrance or entrance <= 50:
    print ("Intervalo (25,50]")
elif 50 > entrance or entrance <= 75:
    print ("Intervalo (50,75]")
elif 75 > entrance or entrance <= 100:
    print ("Intervalo (75,100]")
else:
    print ("Fora de intervalo")