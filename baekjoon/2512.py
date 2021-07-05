import sys

n = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

low = 1
high = max(budgets)

result = 0
while(low<=high):
    mid = (low + high) // 2
    # print("low, high, mid", low, high, mid)
    temp_total = 0
    for budget in budgets:
        if(budget<mid):
            temp_total += budget
        else:
            temp_total += mid
    # print("temp_total: ", temp_total)
    if temp_total<=total:
        result = mid   #result의 정확한 위치??
        # print("result: ", result)
        low = mid+1
    else:
        high = mid-1


print(result)