归并排序是将两个（或两个以上）有序表合并成一个新的有序表，
即把待排序序列分为若干个子序列，每个子序列是有序的。
然后再把有序子序列合并为整体有序序列


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)



def merge(left, right):
    i, j = 0, 0
    # 新建一个数组，用来存储将left和right排好序的值
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':
    list = [2,3,1,4,5]
    print(merge_sort(list))
