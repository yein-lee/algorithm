n = int(input())
a_list = list(map(int, input().split()))

def is_prime_number(i):
    if i == 1:
        return False
    elif i ==2 or i == 3:
        return True
    else:
        for j in range(2, i):
            if i%j==0:
                return False
        return True

cnt = 0
for a in a_list:
    if(is_prime_number(a)):
        cnt += 1

print(cnt)