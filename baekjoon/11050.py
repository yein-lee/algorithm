import sys

n, k = map(int, sys.stdin.readline().split())
k = min(k, n-k)
# result = n*(n-1)*...*(n-k+1)/k*(k-1)*...*1
result = 1
for i in range(n-k+1, n+1):
    result *= i
for i in range(1, k+1):
    result /= i

print(int(result))