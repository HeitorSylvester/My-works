# w = kilos, weights even number of kilos (not obligatory that the parts are equal)
#The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.
#Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos
# and NO in the opposite case.

print ("say yo kilos my mate, of the watermelon ofc")
w = int (input ())
#we need to see the values that can be divided by 2 (like 2, 4, 6...) and see those who are not divided by 2 such as (3,5,7,9) integer

a1 = (w / 2) # division
if 1 <= a1 <= 100 : #1 ≤ w ≤ 100
    print ("i'm above de weight limit")

