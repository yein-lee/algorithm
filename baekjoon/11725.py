import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parent = {}
visited = [False]*(n+1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()
        # print(v, end=' ')
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                parent[node] = v
                visited[node] = True


bfs(1)
# print(parent)
for i in range(2, n+1):
    print(parent[i])