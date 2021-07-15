import sys

n = int(sys.stdin.readline())
cost = [[] for _ in range(n+1)]
dp = [0] * (n+1)
for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    if t+i < n+1:
        cost[t+i].append((t,p))

for i in range(1, n+1):
    temp = 0
    for c in cost[i]:
        if c[1] + dp[i-c[0]] > temp:
            temp = c[1] + dp[i-c[0]]

    dp[i] = max(dp[i-1],temp)

print(dp[n])