import sys

k = int(sys.stdin.readline())
result = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))
