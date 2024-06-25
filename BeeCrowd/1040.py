#entrada:   2 4 7.5 8
grade1, grade2, grade3, grade4 = map(float, input().split())
grade1 *= 2
grade2 *= 3
grade3 *= 4
grade4 *= 1
average = (grade1 + grade2 + grade3 + grade4) / 10
if average >= 7.0:
    print ("Media: %0.1f"% average)
    print ("Aluno aprovado.")
elif average < 4.9:
    print ("Media: %0.1f"% average)
    print ("Aluno reprovado.")
elif average >= 5.0 and average <= 6.9:
    print ("Media: %0.1f"% average)
    print ("Aluno em exame.")    
    exam_grade = float(input())
    result = (average + exam_grade) / 2
    print ("Nota do exame:" , exam_grade)
    print ("Aluno aprovado.")
    print ("Media final: %0.1f"% result)