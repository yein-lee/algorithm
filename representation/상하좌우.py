# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
plans = input().split()
moves = ['L', 'R', 'U', 'D']


x = 0
y = 0
for plan in plans:
    idx = moves.index(plan)
    nx = x + dx[idx]
    ny = y + dy[idx]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(nx+1, ny+1)