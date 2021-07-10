from math import ceil
from sys import stdin

a, b, v = map(int, stdin.readline().split())

print(ceil((v-b)/(a-b)))