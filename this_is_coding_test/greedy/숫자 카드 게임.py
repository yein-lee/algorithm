n, m = map(int, input().split())
max_of_min = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_of_row = min(data)
    max_of_min = max(max_of_min, min_of_row)

print(max_of_min)