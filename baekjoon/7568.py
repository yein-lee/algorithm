import sys

n = int(sys.stdin.readline())
size = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

rank = []
for i in range(n):
    weight, height = size[i][0], size[i][1]
    cnt = 1
    for j in range(n):
        if size[j][0] > weight and size[j][1] > height:
            cnt += 1
    rank.append(cnt)

print(" ".join(map(str, rank)))