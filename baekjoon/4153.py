import sys

while(1):
    lengths = list(map(int, sys.stdin.readline().split()))
    if(lengths[0]==0 and lengths[1]==0 and lengths[2]==0):
        break
    lengths.sort()
    if(lengths[0]**2 + lengths[1]**2 == lengths[2]**2):
        print("right")
    else:
        print("wrong")