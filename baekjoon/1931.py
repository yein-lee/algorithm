import sys
from operator import itemgetter

n = int(sys.stdin.readline())
meetings=list()

for i in range(n):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort(key=itemgetter(1, 0))

cnt = 1
temp_end = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= temp_end:
        temp_end = meetings[i][1]
        cnt += 1

print(cnt)