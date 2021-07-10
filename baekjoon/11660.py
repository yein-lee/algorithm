import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + table[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))