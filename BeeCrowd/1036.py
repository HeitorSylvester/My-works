value_a, value_b, value_c =  map(float, input().split())

bhask1  = (value_b**2 - (4*value_a*value_c))
bhask = -value_b + (bhask1) ** 0.5

if bhask1 < 0 or value_a == 0  :
    print ("Impossivel calcular")
else:
    bhask /= 2*value_a
    
    second_bhask = (value_b**2 - (4*value_a*value_c))
    second_bhask = -value_b - (second_bhask) ** 0.5
    second_bhask /= 2*value_a

    print ("R1 = %0.5f"%bhask)
    print ("R2 = %0.5f"%second_bhask)