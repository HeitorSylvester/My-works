value = int (input())
print (value)
A = int(value / 100)
B = value % 100
print (A, "nota(s) de R$ 100,00")
A = int (B / 50)
B %= 50
print (A, "nota(s) de R$ 50,00")
A = int (B / 20)
B %= 20
print (A, "nota(s) de R$ 20,00")
A = int (B / 10)
B %= 10
print (A, "nota(s) de R$ 10,00")
A = int (B / 5)
B %= 5
print (A, "nota(s) de R$ 5,00")
A = int (B / 2)
B %= 2
print (A, "nota(s) de R$ 2,00")
A = int (B / 1)
B %= 1
print (A, "nota(s) de R$ 1,00")
