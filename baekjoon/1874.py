import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))


for i in range(m):
    # print("i: %d" %i)
    l = 0
    h = n - 1
    while(1):
        mid = (l+h)//2
        if a[mid]==find[i]:
            print(1)
            break
        elif a[mid]<find[i]:
            l = mid + 1
        elif a[mid]>find[i]:
            h = mid - 1

        if(l>h):
            print(0)
            break
