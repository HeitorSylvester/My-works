resquest, amount = map (int, input().split())
if resquest == 1:
    amount *= 4
    print ("Total: R$ %0.2f"%  amount)
elif resquest == 2:
    amount *= 4.50
    print ("Total: R$ %0.2f"%  amount)
elif resquest == 3:
    amount *= 5
    print ("Total: R$ %0.2f"%  amount)
elif resquest == 4: 
    amount *= 2
    print("Total: R$ %0.2f"%  amount)
elif resquest == 5:
    amount *= 1.50
    print ("Total: R$ %0.2f"% amount)