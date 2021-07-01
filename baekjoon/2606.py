import sys
sys.setrecursionlimit(10**7)

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False]*(v+1)
dfs(graph, 1, visited)
cnt = 0
for v in visited:
    if v == True:
        cnt += 1

print(cnt-1)