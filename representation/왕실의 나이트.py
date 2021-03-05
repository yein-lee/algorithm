loc = input()
# x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# x = x_list.index(loc[0])
x = int(ord(loc[0])) - int(ord('a')) #ord()는 아스키코드 값을 반환
y = int(loc[1]) -1

count = 0
moves = [(2,1), (2,-1), (-2,1), (-2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
for move in moves:
    x2 = x + move[0]
    y2 = y + move[1]

    if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
        continue
    count += 1

print(count)