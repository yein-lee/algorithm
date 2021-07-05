import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
digit_plane = list()
numbers = list()

def dfs(x, y, number):
    if len(number)==6:
        if number not in numbers:
            numbers.append(number)
        return

    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]

        if 0<=x2<5 and 0<=y2<5:
            dfs(x2, y2, number+digit_plane[x2][y2])



for i in range(5):
    digit_plane.append(list(map(str, sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        dfs(i, j, digit_plane[i][j])

print(len(numbers))