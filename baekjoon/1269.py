len_a, len_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)
print(len(a-b) + len(b-a))