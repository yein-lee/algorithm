import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
tree = {}

for i in range(n-1):
    p, c, cost = map(int, sys.stdin.readline().split())
    if p in tree:
        tree[p].append((c,cost))
    else:
        tree[p] = [(c,cost)]

    if c in tree:
        tree[c].append((p,cost))
    else:
        tree[c] = [(p,cost)]

length = [0 for _ in range(n+1)]

def dfs(v):
    if v not in tree:
        # print("%d not in tree" %v)
        return
    for child in tree[v]:
        if length[child[0]]==0:
            length[child[0]] = length[v] + child[1]
            dfs(child[0])

dfs(1)
length[1]=0
deepest_node = length.index(max(length))
print(length)
print(max(length))
print(deepest_node)
for i in range(len(length)):
    length[i]=0
print(length)
dfs(deepest_node)
length[deepest_node]=0
print(max(length))

print(length)