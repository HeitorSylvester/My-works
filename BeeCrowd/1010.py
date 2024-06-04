a,b,c = input().split() 
d,e,f = input().split() 
a = int (a)
b = int (b)
c = float(c)
d = int (d)
e = int (e)
f = float (f)
value1 = b * c
value2 = e * f
a_pagar = value1 + value2 
print ("VALOR A PAGAR: R$ %0.2f"% a_pagar)