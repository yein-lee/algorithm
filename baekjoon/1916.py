import sys

INF = 987654321

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

visited = [False]*(n+1)
distance = [0]*(n+1)
graph = [[INF for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
    graph[i][i]=0

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    if cost<graph[a][b]:
        graph[a][b] = cost


start, end = map(int, sys.stdin.readline().split())

def get_smallest_index():
    min = INF
    index = 0
    for i in range(1, n+1):
        if(distance[i]<min and not visited[i]):
            min = distance[i]
            index = i
    return index


def dijkstra(start):
    for i in range(1, n+1):
        distance[i] = graph[start][i]

    visited[start] = True

    for i in range(n):
        current = get_smallest_index()
        visited[current] = True
        for j in range(1, n+1):
            if not visited[j]:
                if (distance[current]+graph[current][j]<distance[j]):
                    distance[j] = distance[current] + graph[current][j]

dijkstra(start)
# print(distance)
print(distance[end])