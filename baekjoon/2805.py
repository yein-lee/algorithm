import sys

n, m = map(int, sys.stdin.readline().split())
height_list = list(map(int, sys.stdin.readline().split()))

def cal_length(height):
    length = 0
    for i in height_list:
        if( (i-height) >= 0):
            length+=i-height
    return length

min_length = 0
max_length = max(height_list)
ans = 0
while(min_length<=max_length):
    mid_length = (min_length + max_length)//2
    if(cal_length(mid_length)>=m):
        min_length = mid_length + 1
        ans = mid_length
    else:
        max_length = mid_length - 1

print(ans)
