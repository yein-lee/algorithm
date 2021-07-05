import sys
from collections import Counter

n = int(sys.stdin.readline())
a_list = list()
for i in range(n):
    a_list.append(sys.stdin.readline())

a_list.sort()

def avg():
    total=0
    for a in a_list:
        total+=a
    return a/4

def median():
    return a_list(n//2)

def mode(): #최빈값
    return 0

def range():
    return a_list[0] - a_list[n-1]