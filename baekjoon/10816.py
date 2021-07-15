import sys

n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))

cards = dict()
for t in temp:
    if t not in cards:
        cards[t] = 1
    else:
        cards[t] += 1

m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
for f in find:
    if f in cards:
        print(cards[f], end=" ")
    else:
        print(0, end=" ")