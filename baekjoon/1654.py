import sys

k, n = map(int, sys.stdin.readline().split())
lan_list = list()
for i in range(k):
    lan_list.append(int(sys.stdin.readline()))

min_length = 1
max_length = max(lan_list)

def is_possible(length):
    cnt = 0
    for i in range(k):
        cnt += lan_list[i]//length

    if cnt>=n:
        return True
    return False

ans = 0
while(min_length<=max_length):
    mid_length = (min_length+max_length)//2
    if(is_possible(mid_length)):
        min_length = mid_length + 1
        ans = mid_length
    else:
        max_length = mid_length - 1

print(ans)


