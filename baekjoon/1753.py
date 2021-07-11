import sys

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

INF = (v-1)*10+1
visited = [False]*(v+1)
graph = [[]*(v+1)]
# graph = [[INF for i in range(v+1)] for j in range(v+1)]
# for i in range(v+1):
#     graph[i][i]=0

for i in range(e):
    a,b,cost = map(int, sys.stdin.readline().split())
    graph[a].append((b,cost))


def dijkstra(start):
    distance = list()
    for i in range(v+1):
        distance.append(graph[start][i])
    # print(distance)
    visited[start]=True

    for i in range(v-1):
        min = INF
        idx=0
        for j in range(1, v):
            if distance[j] < min and not visited[j]:
                min = distance[j]
                idx = j
        visited[idx] = True

        for j in range(1, v+1):
            if not visited[j]:
                if distance[idx] + graph[idx][j] < distance[j]:
                    distance[j] = distance[idx] + graph[idx][j]
    return distance

distance=dijkstra(start)
for i in range(1, v+1):
    if distance[i]!=INF:
        print(distance[i])
    else:
        print("INF")