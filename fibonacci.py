value = int(input())
a, b = 0, 1
print(a)
while value >= b:
    print(b)
    a, b = b, a + b
