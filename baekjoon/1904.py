import sys

n = int(sys.stdin.readline())

dp = list()
dp.append(1)
dp.append(1)

for i in range(2, n+1):
    dp.append((dp[i-1] + dp[i-2])%15746)

print(dp[n])