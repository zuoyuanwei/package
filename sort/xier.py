# 希尔排序，将原始列表分解为多个较小的值列表改进插入排序。
# 最后一步执行完整的插入排序，但是不需要非常多的比较（或移位）
# 因为列表已经被较早的增量插入排序预排序。每个遍历产生比以前一个更有序的列表，使得最终遍历更有效。
# 时间复杂度介于O(n)和O(n^2)。
def shellSort(num):
    sublistcount = len(num)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(num, startposition, sublistcount)
        print('After increments of size', sublistcount, 'The list is', num)
        sublistcount = sublistcount//2
def gapInsertionSort(num, start, gap):
    for i in range(start+gap, len(num), gap):
        currentvalue = num[i]
        position = i
        while position >= gap and num[position-gap] > currentvalue:
            num[position] = num[position-gap]
            position = position - gap
        num[position] = currentvalue


print(shellSort([54,26,93,17,77,31,44,55,20]))