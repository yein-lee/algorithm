import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split()) #[h][n][m]
tomatoes = [[]for i in range(h)]

for i in range(h):
    for j in range(n):
        tomatoes[i].append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(graph, q):
    result = 1
    while(q):
        x, y, z = q.popleft()
        for i in range(6):
            x2 = x + dx[i]
            y2 = y + dy[i]
            z2 = z + dz[i]
            if 0<=x2<h and 0<=y2<n and 0<=z2<m and graph[x2][y2][z2]==0:
                q.append([x2,y2,z2])
                graph[x2][y2][z2] = graph[x][y][z] + 1
                temp = graph[x2][y2][z2]
                if(temp>result):
                    result = temp
    return result

q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 1:
                q.append([i, j, k])

r = bfs(tomatoes, q)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatoes[i][j][k] == 0:
                print(-1)
                exit()
print(r-1)