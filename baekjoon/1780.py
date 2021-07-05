# import collections

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
counts = {-1:0, 0:0, 1:0}

def divide_paper(x, y, n):
    if n==1:
        # print("n is 1")
        counts[paper[x][y]] += 1
        return

    for i in range(x, x+n):
        # print(i)
        for j in range(y, y+n):
            # print(i, j)
            if paper[i][j] != paper[x][y]:
                # print("different value")
                divide_paper(x, y, n//3)
                divide_paper(x, y + n//3, n//3)
                divide_paper(x, y + n*2//3, n//3)

                divide_paper(x + n//3, y, n//3)
                divide_paper(x + n//3, y + n//3, n//3)
                divide_paper(x + n//3, y + n*2//3, n//3)

                divide_paper(x + n*2//3, y, n//3)
                divide_paper(x + n*2//3, y + n//3, n//3)
                divide_paper(x + n*2//3, y + n*2//3, n//3)
                return

    counts[paper[x][y]] += 1

divide_paper(0, 0, n)
# print(counts)
print(counts[-1])
print(counts[0])
print(counts[1])