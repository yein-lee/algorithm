import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
missing = list(map(str, sys.stdin.readline().split()))

def check(num):
    num = list(str(num))
    for i in num:
        if i in missing:
            return False
    return True

result = abs(n-100)

for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i-n))

print(result)