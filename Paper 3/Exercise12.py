print ("digite a quantidade de estudantes da turma")
stu = int (input ())
i = 0 #formação do while 
das = 0 #aux
wir = 0 # ""
mann = 0 # ""
while stu > i :
    nota = int (input ())
    if nota < 0 or nota > 100: 
        print ("-----erro-----")
        break 
    if nota >= das :
        wir = i + 1
        das = nota
    i = i + 1
print ("o aluno com a maior nota foi o aluno " + str (wir)) 