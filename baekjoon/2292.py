n = int(input())

i=0
result=1
while(1):
    result += 6*i
    if n<=result:
        print(i+1)
        break
    i += 1
