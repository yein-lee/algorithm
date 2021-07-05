from collections import deque

MAX = 10**5

def bfs(n, k, cnt):
    q = deque([n])
    while q:
        x = q.popleft()
        # print(x, end=" ")
        if x == k:
            # print()
            print(cnt[x])
            break
        for nx in (x-1, x+1, x*2):
            if nx>=0 and nx<=MAX and cnt[nx]==0:
                cnt[nx] = cnt[x] + 1
                q.append(nx)


cnt = [0] * (MAX+1)
n, k = map(int, input().split())
bfs(n, k, cnt)