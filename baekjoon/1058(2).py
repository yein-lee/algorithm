from collections import deque

def bfs(friends, v, visited):
    visited[v] = True
    q = deque([v])
    cnt = 0
    while q:
        x = q.popleft()
        # print(x, end=' ')
        cnt += 1
        for friend in friends[x]:
            if visited[friend]==False:
                visited[friend] = True
                q.append(friend)
    return cnt


n = int(input())
friends = [[] for i in range(n)]
for i in range(n):
    s = input()
    for j in range(n):
        if s[j]=='Y':
            friends[i].append(j)


result = 0
visited = [False]*n
for i in range(n):
    if visited[i]==False:
        cnt = bfs(friends, i, visited)
        # print("\n\n")
        # print(cnt)
        # print("\n\n")
        if cnt > result:
            result = cnt

if result==0:
    print(result)
else:
    print(result-1)