import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split()) #층, 호수, 손님
    if n%h==0:
        a = n//h
        b = h
    else:
        a = n//h+1
        b = n%h
    if a<10:
        print("{}0{}".format(b,a))
    else:
        print("{}{}".format(b,a))