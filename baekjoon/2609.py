import sys

n, m = map(int, sys.stdin.readline().split())

a, b = n, m

while b!=0:
    a = a%b
    a,b = b,a

print(a)
print(n*m//a)


