entrance_1,entrance_2,entrance_3 = map (int,(input().split()))
if entrance_1 > entrance_2 and entrance_1 > entrance_3:
    print(entrance_1)
if entrance_2 > entrance_1 and entrance_2 > entrance_3:
    print(entrance_2)
if entrance_3 > entrance_2 and entrance_3 > entrance_2:
    print(entrance_3)