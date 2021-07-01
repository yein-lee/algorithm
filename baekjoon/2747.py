import sys

n = int(sys.stdin.readline())

x = 0
y = 1

for i in range(2, n+1):
    x, y = y, (x+y)

print(y)