c = 10
print(id(c))

def check_id(c):
    print(id(c))
    c = 20
    print(id(c))

check_id(c)
print(c)
print(id(c))