首先取一个正数d1 = n/2，将元素分为d1个组，每组相邻元素之间的距离为d1，在各组内进行直接插入排序
取第二个正数d2 = d1 / 2，重复上述分组排序过程，直到di = 1,即所有的元素都在同一组进行直接插入排序。
希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序，最后一趟排序使得所有数据有序

a = [2,3,1,4,5]
# dk为步长
dk = len(a)//2
while dk >= 1:
    for i in range(dk,len(a)):
        temp = a[i]
        j = i - dk
        while j >= 0 and temp < a[j]:
            a[j+dk] = a[j]
            j -= dk
        a[j+dk] = temp
    dk = dk//2
print(a)