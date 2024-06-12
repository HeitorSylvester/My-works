answers=input("Digite o gabarito: ").split() #gabarito
qty_students=int(input()) #quantidade de alunos
#questoes 6, de A até E
i=0
vector=[]
while qty_students>i:
    student_answers=input()
    student_answers=student_answers.split()
    vector.append(student_answers)
    i+=1


i=0
while i < qty_students:
    j=0
    acertos=0
    while j < len(answers):
        if answers[j] == vector[i][j]:
            acertos+=1
        j+=1
    print (acertos)
    i+=1