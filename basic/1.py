def solution(left, right):
    answer = 0

    for temp in range(left, right + 1):
        print(temp, end=": ")
        cnt = 0
        for i in range(1, temp + 1):
            if temp % i == 0:
                print(i, end=" ")
                cnt += 1
        print(cnt)
        if cnt % 2==0:
            answer += temp
        else:
            answer -= temp
        print(answer)
    return answer


print(solution(13, 17))