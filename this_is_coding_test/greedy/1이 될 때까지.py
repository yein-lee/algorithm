n, k = map(int, input().split())
cnt = 0

while(n!=1):
    if n % k == 0 :
        cnt += 1
        n = n // k
    else:
        n -= 1

print(cnt)
# n=25
# k=5
# print(n//k)