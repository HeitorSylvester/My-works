#entrada de valor 16 2 hora inicial e hora final
start,end = map(int, input().split()) 
if start > end or start == end:
    result = end - start
    result += 24
elif start < end:
    result = end - start  
print(f"O JOGO DUROU {result} HORA(S)")