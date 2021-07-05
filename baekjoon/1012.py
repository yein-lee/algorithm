import sys
sys.setrecursionlimit(10**7)

def dfs(cabbage, i, j):
    if i<0 or i>=n or j<0 or j>=m or cabbage[i][j]!=1:
        return
    # print("x, y: %d, %d" %(j, i))
    cabbage[i][j] = 0
    dfs(cabbage, i+1, j)
    dfs(cabbage, i-1, j)
    dfs(cabbage, i, j+1)
    dfs(cabbage, i, j-1)


t = int(input())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    cabbage = [[0 for i in range(m)]for i in range(n)]

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        cabbage[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cnt += 1
                dfs(cabbage, i, j)
    print(cnt)