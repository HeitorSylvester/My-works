i = 0
vector = []
while 100 > i:
    values = float (input()) 
    vector.append(values) 
    if vector [i] <= 10:
        print ("A" + "["+ str (i) + "] = " + "%0.1f" % (vector[i]) )
    i+=1 