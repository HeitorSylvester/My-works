idade_dias = int (input()) #400
anos = idade_dias // 365
resto = idade_dias % 365
meses = resto // 30
dias = resto % 30
print (anos, "ano(s)")
print (meses, "mes(es)")
print (dias, "dia(s)")