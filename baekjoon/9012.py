import sys

n = int(sys.stdin.readline())

for i in range(n):
    ps = sys.stdin.readline()
    stack = list()
    flag = True
    for j in range(len(ps)):
        if ps[j] == '(':
            stack.append(ps[j])
        elif ps[j] ==')':
            if not stack:
                flag = False
                break
            if stack.pop() != '(':
                flag = False
                break
    if stack:
        flag = False
    if flag:
        print('YES')
    else:
        print('NO')