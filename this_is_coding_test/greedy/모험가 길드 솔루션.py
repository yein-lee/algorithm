n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 그룹 수
count = 0 # 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i: #현재 그룹에 포함된 모험가의 수가 공포도 이상이면 그룹 결성
        result += 1
        count = 0