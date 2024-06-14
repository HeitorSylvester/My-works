a,b,s=input().split()
a=int(a)
b=int(b)
s=int(s)
maiorAB = (a + b+ abs(a-b)) /2
bigger = (maiorAB + s + abs (maiorAB - s))/2
print (int (bigger), "eh o maior")