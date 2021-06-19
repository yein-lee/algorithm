l = int(input())
s = input()

r = 31
m = 1234567891

hash = 0
for i in range(l):
    hash += (ord(s[i]) - ord('a') + 1)*pow(r,i)
print(hash%m)