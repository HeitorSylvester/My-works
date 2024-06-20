answers = input().split() #respostas dos alunos
amount_students = int(input())
i = 0 
j = 0
aux = 0
while amount_students > i:
    student_answers = input().split()
    while amount_students > j:
        if student_answers[j] == answers[i]:
            aux += 1
        j += 1 
    print (aux)
    i+=1  
