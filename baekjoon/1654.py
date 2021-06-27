import sys

n, m = map(int, sys.stdin.readline().split())
lan_list = list()

for i in range(n):
    lan_list.append(int(sys.stdin.readline()))

print(lan_list)
max_legnth = max(lan_list)
min_length = 1


def is_available(len):
    cnt = 0
    for lan in lan_list:
        cnt += lan // len

    if cnt >= m:
        return True
    else:
        return False

result = 0
while(min_length<=max_legnth):
    mid = (min_length + max_legnth)//2
    if(is_available(mid)):
        min_length = mid + 1
    else:
        max_legnth = mid -1

print(mid)
