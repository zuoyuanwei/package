# 选择排序，一次遍历后选择最大的项放在正确的位置，下一次遍历选择次最大的项放在正确位置。
# 时间复杂度和冒泡一样O(n^2)，但是交换数量更少，选择排序通常在基准研究中执行更快。
def selectionSort(num):
    for fillslot in range(len(num)-1, 0, -1):
        positionofMax = 0
        for location in range(1, fillslot+1):
            if num[location] > num[positionofMax]:
                positionofMax = location
        num[fillslot], num[positionofMax] = num[positionofMax], num[fillslot]
    return num


print(selectionSort([54,26,93,17,77,31,44,55,20]))