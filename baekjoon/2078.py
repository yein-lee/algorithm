
a, b = map(int, input().split())
x = 0
y = 0

while(1):
    # print("%d %d" %(n, m))
    if(a==1):
        y += b-1
        break
    elif(b==1):
        x += a-1
        break
    if(a>b):
        a = a%b
        x += int(a/b)
        print("a: %d" %a)
        print("x: %d" %x)
    else:
        b = b%a
        y += int(b/a)
        print("b: %d" %b)
        print("y: %d" %y)



print("%d %d" %(x, y));


