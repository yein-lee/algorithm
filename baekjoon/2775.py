import sys

t = int(sys.stdin.readline())
k = list()
n = list()

for i in range(t):
    k.append(int(sys.stdin.readline())) #층
    n.append(int(sys.stdin.readline())) #호

k_max = max(k)
n_max = max(n)

apartment = [[0 for i in range(n_max+1)] for j in range(k_max+1)]

for i in range(n_max+1):
    apartment[0][i] = i

for i in range(1, k_max+1):
    for j in range(1, n_max+1):
        for l in range(1, j+1):
            apartment[i][j] += apartment[i-1][l]

for i in range(t):
    print(apartment[k[i]][n[i]])
