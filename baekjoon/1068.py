import sys

count = 0
def dfs(v, tree, visited):
    if v not in tree or not tree[v]:
        global count
        count += 1
        return

    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            dfs(i, tree, visited)


n = int(sys.stdin.readline())
parent_nodes = tuple(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())

tree = {}
visited = [False]*n

for i in range(0, n):
    if i!=delete_node and parent_nodes[i]!=delete_node:
        if parent_nodes[i] in tree:
            tree[parent_nodes[i]].append(i)
        else:
            tree[parent_nodes[i]] = [i]

if -1 not in tree:
    print(0)
    exit()

for i in tree[-1]:
    dfs(i, tree, visited)

print(count)