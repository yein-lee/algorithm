import sys

n = int(sys.stdin.readline())
a_list = list()
for i in range(n):
    a_list.append(int(sys.stdin.readline()))

a_list.sort()

for a in a_list:
    print(a)