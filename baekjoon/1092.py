import sys

n = int(sys.stdin.readline())
weight_limit = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
weight_of_box = list(map(int, sys.stdin.readline().split()))

weight_limit.sort(reverse=True)
weight_of_box.sort(reverse=True)
print(weight_limit)
print(weight_of_box)

if(weight_of_box[0]>weight_limit[0]):
    print(-1)
    exit()

cnt=0

while(weight_of_box):
    cnt += 1
    j=0
    print("cnt: ", cnt)
    for limit in weight_limit:
        for j in range(len(weight_of_box)):
            if limit>
print(cnt)


