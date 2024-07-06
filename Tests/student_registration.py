print ("********* Olá, qual será a ação hoje? *******")
print ("  CADASTRO      --------- 1") #cadastro feito
print (" EDITAR ALUNO   --------- 2") #editar aluno
print (" REMOVER ALUNO  --------- 3") 
print ("LISTA DE ALUNOS --------- 4") #lista de alunos fazer
print ("*******************************************")
print ("ver. 0.0.1")


entrance = int (input()) #fazer um cadastro
#THE INTERFACE

#THE MENU INPUTS
register = 1
edit_user = 2
remove_user = 3
student_lists = 4
answer = True 
#THE MENU ENTRANCE
while answer == True:# AQUI ESTÃO AS ENTRADAS DO MENU PRINCIPAL
    if register == 1:
        #THE REGISTER MENU
        print ("*************** CADASTRO ***************")
        student_name = input ("             DIGITE O NOME COMPLETO  \n").split()
        id = int(input ("         DIGITE O CPF DO ALUNO \n"))
        subs = input ("DIGITE A DICIPLINA PARA APLICAÇÃO (PARA MAIS DE UMA DICIPLINA ESCREVA COM ESPAÇOS) \n").split()
        print ("*******************************************")
    elif edit_user == 2:
        answer = False
    elif remove_user == 3:
        answer = False
    elif student_lists == 4:
        answer == False