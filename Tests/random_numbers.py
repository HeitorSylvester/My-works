# This's a random number generator for doing exercises on beecrowd, idk i just wanted to do it lol
import random
entrance = int(input("Type a Random number and see your Beecrowd quest:\n"))
i=0
while entrance > i :
    value = random.randint(1001, 3099)
    i+=1
print ("YOUR BEECROWD EXERCISE OF THE DAY WILL BE..... \n")
print ("********************")
print ("https://judge.beecrowd.com/pt/problems/view/%0.0f \n"% value)
print ("********************")