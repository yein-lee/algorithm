import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]



for i in range(1, n):
    for j in range(1, n):
        table[i][j] += table[i][j-1]
        table[i][j] += table[i-1][j]
