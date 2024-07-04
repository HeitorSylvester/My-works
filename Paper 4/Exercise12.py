numeros = input ()
valores = numeros.split()
i = 0
while i < len(valores):
    alvo = valores [i]
    j = 0
    contador = 0

    while j < len (valores):
        if valores [j] == alvo:
            contador +=1
    
        print(alvo + "aconteceu" + str (contador) + "vez(es)")
        i+= 1