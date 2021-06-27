import sys

m, n = map(int, sys.stdin.readline().split())

chess = list()
for i in range(m):
    chess.append(input())

def cal_repaint_n(x, y):
    black_n1 = 0
    white_n1 = 0

    #case 1
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            # print("x, y: %d, %d" % (x + i, y + j))
            if(chess[x+i][y+j]=='W'):
                black_n1 += 1

    for i in range(1, 8, 2):
        for j in range(1, 8, 2):
            if(chess[x+i][y+j]=='W'):
                black_n1 += 1

    for i in range(0, 8, 2):
        for j in range(1, 8, 2):
            if(chess[x+i][y+j]=='B'):
                white_n1 += 1

    for i in range(1, 8, 2):
        for j in range(0, 8, 2):
            if(chess[x+i][y+j]=='B'):
                white_n1 += 1

    return min(white_n1+black_n1, 64- white_n1 - black_n1)


#x가 가질 수 있는 값 0 ~ m-8
#y가 가질 수 있는 값 0 ~ m-8

min_ = 32
for i in range(0, m-7):
    for j in range(0, n-7):
        temp = cal_repaint_n(i, j)
        if(temp<min_):
            min_ = temp

print(min_)