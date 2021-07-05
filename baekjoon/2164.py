from collections import deque

n = int(input())
d = deque([i for i in range(1, n+1)])
print(d)
for i in range(n-1):
    d.popleft()
    d.append(d.popleft())

print(d[0])