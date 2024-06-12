n = int(input()) #556
horas = n // 3600
resto = n % 3600 
minutos = resto // 60
segundos = resto % 60
print (f"{horas}:{minutos}:{segundos}") # <--- Template string