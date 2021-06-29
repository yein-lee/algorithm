e = int(input())
v = int(input())
graph = {}
for i in range(v):
    v[i] = []

for i in range(v):
    a, b = map(int, input().split())
    v[a].append(b)

print(graph)
