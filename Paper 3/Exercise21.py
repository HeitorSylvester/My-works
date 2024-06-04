def conta_digitos (n , d):
# n e d são inteiros 
#d = 5, n = 3426 
# 3426 % 10 --> 6 == 5 ?
# 342 % 10 --> 2 == 5 ?
# 34 % 10 --> 4 == 5 ?
# 3 % 10 --> 3 == 5 ?
# 0 
    contador = 0 
    while n != 0:
        digito = n % 10 
        if digito == d :
            contador = contador + 1 
        n = int (n/10)
        return contador 
def conta_digito_total (n):
    contador = 0 
    while n != 0 :
        n = int (n/10)
        contador = contador + 1
    return contador
# a = 541234
print ("Digite o A")
a = int (input())
# 4321445
print ("Digite o B")
b = int (input())

eh_permutação = True 

if conta_digito_total(a) != conta_digito_total(b):
    eh_permutação = False  

# a_mutante = 5412434
a_mutante = a
while eh_permutação and a_mutante != 0:
    #extrair um digito d de a 
    # d = 4 
    d = a_mutante % 10
    # contar quantas vezes d acontece em a 
    contagem_a = conta_digitos (a, d)
    #contar quantas vezes d acontece em b 
    contagem_b = conta_digitos (b, d)
    #verificar se é igual 
    if contagem_a != contagem_b:
        eh_permutação = False 

    a_mutante = int (a_mutante/10)

if eh_permutação:
    print ("É permutação")
else :
    print ("Não é permutação")