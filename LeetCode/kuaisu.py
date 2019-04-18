选择一个基准元素，通常选择第一个元素或者最后一个元素
通过一趟排序将待排序的记录分割成独立的两部分，其中一部分的记录值均比基准元素小，另一部分元素值均比基准元素大
此时基准元素在其排好序后的正确位置
然后分别堆这两部分用同样的方法继续进行排序，直到整个序列有序

list = [2,3,1,4,5]


def quick_sort(list, left, right):
    if left < right:
        mid = partition(list, left, right)
        quick_sort(list, 0, mid - 1)
        quick_sort(list, mid + 1, right)
    return list


def partition(list, left, right):
    temp = list[left]
    while left < right:
        while left < right and list[right] >= temp:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= temp:
            left += 1
        list[right] = list[left]
    list[left] = temp
    return left

if __name__ == '__main__':
    quick_sort(list,0,len(list)-1)
    print(list)