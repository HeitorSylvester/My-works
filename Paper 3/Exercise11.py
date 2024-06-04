#revisar esse exercicio mas ok...

i = 0 #formação do while 
aux = 0 # auxiliar
das = 0 #aux 
wir = 0 # ""
while 7 > i :
    ent = int (input ())
    das = ent + das
    if ent >= aux :
        wir = i + 1
        aux = ent
    i = i + 1
print ("o dia com mais vendas é o dia " + str (wir) )
print ("foram vendidos  " + str (das) + "  discos")