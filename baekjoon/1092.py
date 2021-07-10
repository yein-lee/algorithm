import sys

n = int(sys.stdin.readline())
limits = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))

limits.sort(reverse=True)
weights.sort(reverse=True)

if weights[0]>limits[0]:
    print(-1)
    exit()

result = 0
while(weights):
    i, j = 0, 0
    while(i<n and j<len(weights)):
        if(weights[-1]>limits[i]):
            break
        if(limits[i]>=weights[j]):
            i += 1
            weights.pop(j)
        else:
            j += 1
    result += 1

print(result)
