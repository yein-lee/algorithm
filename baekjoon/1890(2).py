import sys

n = int(sys.stdin.readline())
a = []
b = [[n*n for i in range(n)] for i in range(n)]
b[0][0] = 0
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
# print(a)
# print(b)
cnt = 0
def dp(x, y):
    global cnt
    cnt += 1
    distance = a[x][y]
    # print("x, y: %d, %d" %(x, y))
    if(distance==0):
        return True
    if distance <= n - x - 1:
        # 아래로 간다.
        b[x + distance][y] = min(b[x][y] + 1, b[x + distance][y])
        # print("b[%d][%d]: %d" % (x+distance, y, b[x+distance][y]))
        dp(x + distance, y)

    if distance <= n - y - 1:
        # 아래로 간다
        b[x][y + distance] = min(b[x][y] + 1, b[x][y + distance])
        # print("b[%d][%d]: %d" %(x, y+distance, b[x][y+distance]))
        dp(x, y + distance)


x, y = 0, 0
dp(0, 0)
# print(b)
print(b[n-1][n-1])
print(cnt)