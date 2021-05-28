n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
sum=0

while True:
    for i in range(k):
        if (m <= 0):
            break
        sum += data[0]
        m -= 1
    if (m <= 0):
        break
    sum += data[1]
    m -= 1



print(sum)

