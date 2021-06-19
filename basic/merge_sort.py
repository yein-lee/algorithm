def merge_sort(list):
    if len(list)<=1:
        return list
    mid = len(list)//2
    left_list = list[:mid]
    right_list = list[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    result = list()
    while len(left_list) > 0 or len(right_list):
        if len(left_list)>0 and len(right_list):
            print(1)
            if left_list[0] <= right_list[0]:
                result.append(left_list[0])
                left_list = left_list[1:]
            else:
                result.append(right_list[0])
                right_list = right_list[1:]
        elif len(left_list) > 0:
            print(2)
            result += left_list
            left_list.clear()
        elif len(right_list) > 0:
            print(3)
            result += right_list
            right_list.clear()
    return result