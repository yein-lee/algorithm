import sys
from operator import itemgetter

n = int(sys.stdin.readline())
members = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), str(name)))
members.sort(key=itemgetter(0))

for age, name in members:
    print(age, name)