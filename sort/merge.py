# 归并排序，分而治之，最坏时间复杂度为O(nlgn)。
# 拆分的操作需要lgn，合并需要n操作。
# 归并排序需要额外的空间来保存两个半部分，因为是切片操作提取，如果列表很大，空间需求就会很大。
class MergeSort:
    def mergesort(self, num):
        if len(num) <= 1:
            return num
        mid = len(num)//2
        left = self.mergesort(num[:mid])
        right = self.mergesort(num[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:]
        res += right[j:]
        return res


if __name__ == "__main__":
    num = [5, 2, 4, 6, 1, 3, 7]
    M = MergeSort()
    print(M.mergesort(num))