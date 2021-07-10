import sys
from operator import itemgetter

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    new_recruits = list()
    for i in range(n):
        new_recruits.append(tuple(map(int, sys.stdin.readline().split())))

    new_recruits.sort(key=itemgetter(0,1))

    cnt=0

    for i in range(1, n):
        for j in range(0, i):
            if new_recruits[j][0] < new_recruits[i][0] and new_recruits[j][1] < new_recruits[i][1]:
                break
            if(j==i-1):
                cnt += 1

    print(cnt)