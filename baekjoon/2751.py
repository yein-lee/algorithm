import sys

n = int(sys.stdin.readline())
numbers = list()
for i in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for number in numbers:
    print(number)