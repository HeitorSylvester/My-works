idade_dias = int (input()) #400
anos = idade_dias // 365
resto = idade_dias % 365
meses = 0
dias = resto % 30
print (anos, "ano(s)") 
if idade_dias < 31:
    meses = idade_dias // 30
    print (meses,"mes(es)")
else:
    meses = anos % 30 
    print (meses,"mes(es)")
dias = resto % 30
print (dias,"dia(s)")  
