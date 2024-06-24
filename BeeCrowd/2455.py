#uso da formula P1 ∗ C1 = P2 ∗ C2
a, b ,c , d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
left_sesaw = a * b 
right_sesaw = c * d
if left_sesaw > right_sesaw:
    print ("-1")
elif left_sesaw < right_sesaw:
    print ("1")
else:
    print ("0")