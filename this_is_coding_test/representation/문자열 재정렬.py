s = input()
sorted_list = []
value = 0

for i in range(len(s)):
    if s[i].isalpha():
        sorted_list.append(s[i])
    else:
        value += int(s[i])

sorted_list.sort()
if value is not 0:
    sorted_list.append(str(value))
    # sorted_list.append(str(value))

print(''.join(sorted_list))
