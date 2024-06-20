entrance_1,entrance_2,entrance_3 = input().split()
entrance_1=int(entrance_1)
entrance_2=int(entrance_2)
entrance_3=int(entrance_3)
aux = 0
aux_2 = 0 
aux_3 = 0
if entrance_1 > entrance_2 and entrance_1 > entrance_3: #maior valor fixo
    aux = entrance_1
    print (aux)

if aux > entrance_2:
    aux_2 = entrance_2
    print (aux_2)
elif aux > entrance_3:
    aux_2 = entrance_3
    print (aux_2)