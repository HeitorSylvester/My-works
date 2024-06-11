answers=input("Digite o gabarito: ") #gabarito
qty_students=int(input()) #quantidade de alunos
#questoes 6, de A até E
i=0
vector=[]
answers.split()
print (answers)
while qty_students>i:
    student_answers=input()
    student_answers=student_answers.split()
    i-=1
i=0

while qty_students>i:
    print (vector[0],student_answers[0])
    i+=1