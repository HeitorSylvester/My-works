value = float (input())
print (value)
A = float(value / 100)
B = value % 100
print ("%0.4f"% A, "nota(s) de R$ 100,00")
A = float (B / 50)
B %= 50
print ("%0.4f"% A, "nota(s) de R$ 50,00")
A = float (B / 20)
B %= 20
print ("%0.4f"% A, "nota(s) de R$ 20,00")
A = float (B / 10)
B %= 10
print ("%0.4f"% A, "nota(s) de R$ 10,00")
A = float (B / 5)
B %= 5
print ("%0.4f"% A, "nota(s) de R$ 5,00")
A = float (B / 2)
B %= 2
print ("%0.4f"% A, "nota(s) de R$ 2,00")
print ("MOEDAS")
A = float (B / 1)
B %= 1
print ("%0.4f"% A, "moeda(s) de R$ 1.00")
A = float (B / 0.50)
B %= 0.50
print ("%0.4f"% A, "moeda(s) de R$ 0.50")
A = float (B / 0.25)
B %= 0.25
print ("%0.4f"% A, "moeda(s) de R$ 0.25")
A = float (B / 0.10)
B %= 0.10
print (A, "moeda(s) de R$ 0.10")
A = float (B / 0.05)
B %= 0.05
print ("%0.4f"% A, "moeda(s) de R$ 0.05")
A = float (B / 0.01)
B %= 0.01
print ("%0.4f"% A, "moeda(s) de R$ 0.01 ")