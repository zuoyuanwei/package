每一趟（例如第i趟）在后面n-i+1(i=1,2,…,n-1)个待排序元素中选取关键字最小的元素，
作为有序子序列的第i个元素，直到n-1趟做完，就不用再选了。

a = [2,4,1,3,5]
for i in range(len(a)-1):
    min = i
    for j in range(i+1,len(a)):
        if a[j] < a[min]:
            min = j
    a[i],a[min] = a[min],a[i]
print(a)

注：min改为max，小于改为大于可以实现从大到小排序。