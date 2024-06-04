a,b,c = input().split()
a=float(a)
b=float(b)
c=float(c)
triangle = (a*c)/2 
circle = 3.14159*(c**2)
trapzoid =(a+b)/2*c  
square = b ** 2
rectangle = a * b
print ("TRIANGULO: %0.3f"% triangle)
print("CIRCULO: %0.3f"% circle)
print ("TRAPEZIO: %0.3f"% trapzoid)
print ("QUADRADO: %0.3f"% square)
print ("RETANGULO: %0.3f"% rectangle)