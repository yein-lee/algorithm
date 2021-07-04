import sys
n, c = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]

def router_counter(distance):
    count = 1
    cur_house = house[0]
    for i in range(1, n):
        if cur_house + distance <= house[i]:
            count += 1
            cur_house = house[i]
    return count

house.sort()
start, end = 1, house[-1]-house[0]


while(start<=end):
    mid = (start+end)//2
    if router_counter(mid) >= c:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)