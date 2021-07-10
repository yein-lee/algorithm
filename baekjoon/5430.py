import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    cmds = list(map(str, sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline())

    flag = True
    if n!=0:
        nums = deque(list(map(int, sys.stdin.readline().lstrip('[').rstrip().rstrip(']').split(","))))
        for cmd in cmds:
            if cmd == 'R':
                nums.reverse()
            elif cmd == 'D':
                if nums:
                    nums.popleft()
                else:
                    flag = False
                    break
    else:
        nums = sys.stdin.readline()
        flag=False

    if flag:
        print('[', end="")
        if nums:
            for i in range(len(nums)-1):
                print(nums[i], end="")
                print(",", end="")
            print(nums[-1], end="")
        print("]")
    else:
        print('error')