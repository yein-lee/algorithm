n = int(input())
cost = list(map(int, input().split()))
money = int(input())
biggest = 0
min_cost = min(cost)



for i in range(n):
    print(money)
    print(cost[n-1-i])
    print(n-1-i)
    biggest += (money//cost[n-1-i])*(n-1-i)
    money = money%cost[n-1-i]

print(biggest)