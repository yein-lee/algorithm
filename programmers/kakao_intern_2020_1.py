def solution(numbers, hand):
    answer = ''

    x1, y1 = 3, 0 #왼손의 좌표
    x2, y2 = 3, 2 #오른손의 좌표
    x, y = 0, 0

    for n in numbers:
        #왼손
        if n ==1:
            x1, y1 = 0, 0
            answer += 'L'
        elif n==4:
            x1, y1 = 1, 0
            answer += 'L'
        elif n==7:
            x1, y1 = 2, 0
            answer += 'L'

        #오른손
        elif n==3:
            x2, y2 = 0, 2
            answer += 'R'
        elif n==6:
            x2, y2 = 1, 2
            answer += 'R'
        elif n==9:
            x2, y2 = 2, 2
            answer += 'R'

        #왼손 or 오른손
        else:
            if n==2:
                x, y = 0, 1
            elif n==5:
                x, y = 1, 1
            elif n==8:
                x, y = 2, 1
            elif n==0:
                x, y = 3, 1

            left_move = abs(x1-x) + abs(y1-y)
            right_move = abs(x2-x) + abs(y2-y)
            if left_move<right_move:
                x1, y1 = x, y
                answer += 'L'
            elif left_move>right_move:
                x2, y2 = x, y
                answer += 'R'
            else:
                if hand == 'left':
                    x1, y1 = x, y
                    answer += 'L'
                else:
                    x2, y2 = x, y
                    answer += 'R'

    return answer