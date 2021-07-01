import sys

n, m = map(int, sys.stdin.readline().split())

not_heard = list()
not_seen = list()

for i in range(n):
    not_heard.append(sys.stdin.readline())

for j in range(m):
    not_seen.append(sys.stdin.readline())

both = list(sorted(set(not_heard).intersection(not_seen)))
print(len(both))
print("".join(both))