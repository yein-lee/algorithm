import sys

while(1):
    line = sys.stdin.readline()
    if line == ".":
        break

    stack = list()
    flag = True
    for a in line:
        if a == '(' or a == '[':
            stack.append(a)
        elif a == ')':
            if not stack or stack[-1]!='(':
                flag = False
                break
            stack.pop()
        elif a == ']':
            if not stack or stack[-1]!='[':
                flag = False
                break
            stack.pop()
    if stack:
        flag = False

    if flag==True:
        print('yes')
    else:
        print('no')