n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()

sum = 0
for i in range(n):
    for j in range(0, i+1):
        sum += time_list[j]

print(sum)