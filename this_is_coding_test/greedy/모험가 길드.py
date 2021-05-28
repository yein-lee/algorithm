n = int(input())
f = map(int, input().split())
f.sort()
cnt = 0
i = 0
while True:
    n -= f[i]
    i += f[i]
    if n <= 0:
        break
    cnt += 1