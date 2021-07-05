n = int(input())
friends = [[] for i in range(n)]

for i in range(n):
    s = input()
    for j in range(n):
        if s[j]=='Y':
            friends[i].append(j)

def dfs(friends, v, visited, cnt):
    visited[v] = True
    cnt += 1
    # print(v, end=' ')
    for i in friends[v]:
        # print("friends: %d" %i)
        if visited[i]==False:
            # print("visited false")
            cnt = dfs(friends, i, visited, cnt)
    return cnt

result = 0
visited = [False]*n
for i in range(n):
    # if visited[i] == False:
    cnt = 0
    cnt = dfs(friends, i, visited, cnt)
    if cnt > result:
        result = cnt

if result==0:
    print(result)
else:
    print(result-1)