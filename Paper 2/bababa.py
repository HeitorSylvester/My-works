print("digite um número:")
x= int(input())
print("digite um número:")
y= int(input())
print("digite um número:")
z= int(input())
if z<  y and z<x:#z sendo o número maior
    if y<x:
        print(z,y,x)
    elif x<y:
        print(z,x,y)     

if y<z and y<x:#y sendo o número maior
    if z<x:
        print(y,z,x)
    elif x<z:
        print (y,x,z)

if z<y and y<x:#x sendo o número maior
    if z<y:
        print (x,z,y)
    elif y < z:
        print (x,y,z)
    