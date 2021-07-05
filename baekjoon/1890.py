import sys

n = int(sys.stdin.readline())
a = []
b = [[0 for i in range(n)] for i in range(n)]
b[0][0] = 1
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
# print(a)
# print(b)

for i in range(n):
    for j in range(n):
        distance = a[i][j]
        if(distance==0):
            break
        if(b[i][j]==0):
            continue
        else:
            if distance < n-j:
                b[i][j+distance] += b[i][j]
            if distance < n-i:
                b[i+distance][j] += b[i][j]


print(b[-1][-1])