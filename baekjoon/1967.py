import sys

n = int(sys.stdin.readline())
tree = {}

for i in range(n-1):
    p, c, cost = map(int, sys.stdin.readline().split())
    if p in tree:
        tree[p].append((c,cost))
    else:
        tree[p] = [(c,cost)]


for child in tree[1]:
    print(child)
    print(child[0])
    print(child[1])


longest = 0
def dfs(v):
    while(1):
        if v not in tree:
            break
        max_cost = 0
        for child in tree[v]:
            if child[1]>max_cost:
                max_node = child[0]
                max_cost = child[1]
        v=max_node
        print(max_node, end=' ')
        global longest
        longest += max_cost


print(tree)
dfs(1)
print(longest)