numeros = input ()
valores = numeros.split()
i = 0
aux_vector = []
while i < len(valores):
    aux_vector.append(valores[i])
    contador = 0
    j = 0
    while j < len (valores):
        if valores [j] == aux_vector[i]:
            contador +=1
        j+=1
    print(aux_vector[i], " aconteceu " + str (contador) + " vez(es)")
    i+= 1

        
        
        