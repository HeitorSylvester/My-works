continua = True 
mensagem = ""
numero = int(input())
while continua:
    mensagem = mensagem + str (numero) + ";"
    try: #<---- NOVO
        numero = int(input())
    except EOFError: #<---- NOVO
        continua = False

#USO LINCADO COM O ARQUIVO (entrada.txt) 