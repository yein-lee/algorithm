import sys

a, b = map(int, sys.stdin.readline().split())

common_factor = min(a, b)     #공약수
common_multiple = max(a, b)   #공배수

while(1):
    if(a%common_factor==0 and b%common_factor==0):
        break
    common_factor -= 1

while(1):
    if(common_multiple%a==0 and common_multiple%b==0):
        break
    common_multiple += 1

print(common_factor)
print(common_multiple)



