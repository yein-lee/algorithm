from collections import deque

n = 10 #n은 노드(vertex)의 개수 (1부터 n까지 순차적으로 증가한다는 가정 하에)
visited = [False]*(n+1)
graph = [[]] #인접리스트

def bfs(v): #인접리스트
    q = deque([v])
    visited[q] = True

    while q:
        v=q.popleft()
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

#인접행렬