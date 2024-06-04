dias = 7 
i = 0 #formação do while 
temps = 0 #temperaturas da semana (médias)
aux = 0 # auxiliar
helpi = 0 #auxiliar 
while dias > i :
    temps = float (input()) # entrada nas temps da semana
    aux = temps + aux 
    i = i + 1


helpi = aux / 7
if helpi > 25 :
        print ("pouca probabilidade de ter temperaturas negativas")
elif helpi < 24:
        print ("há uma chance de 2 temperaturas negativas")
elif helpi < 22 :
        print ("há uma chance de ter mais de 3 temperaturas negativas")