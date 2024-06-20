# Lê as respostas corretas
answers = input().split()

# Lê a quantidade de alunos
amount_students = int(input())

# Lista para armazenar as respostas dos alunos
students_answers = []

# Loop para coletar as respostas dos alunos
i = 0
while i < amount_students:
    student_answers = input().split()
    students_answers.append(student_answers)
    i += 1

# Processamento das respostas para contagem de acertos e impressão das respostas dos alunos
i = 0
while i < amount_students:
    student_answers = students_answers[i]
    j = 0
    correct_count = 0

    while j < len(answers):
        if student_answers[j] == answers[j]:
            correct_count += 1
        j += 1
    
    # Imprime a quantidade de acertos do aluno
    print(correct_count)
    i += 1
