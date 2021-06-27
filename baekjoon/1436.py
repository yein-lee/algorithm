n = int(input())
cnt = 0
six_sixes = 666

while(1):
    if '666' in str(six_sixes):
        cnt+=1
    if cnt == n:
        print(six_sixes)
        break
    six_sixes += 1