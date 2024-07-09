numeros = input()
valores = numeros.split()
i = 0
processados = []

while i < len(valores):
    alvo = valores[i]
    ja_processado = False
    k = 0
    while k < len(processados):
        if processados[k] == alvo:
            ja_processado = True
        k += 1
    if ja_processado == False:
        contador = 0
        j = 0
        while j < len(valores):
            if valores[j] == alvo:
                contador += 1
            j += 1
        print(alvo + " acontece " + str(contador) + " vez(es)")
        processados.append(alvo)
    i += 1
