# 快速排序算法，最坏时间复杂度为O(n^2)。
# 数据越随机分布时，快速排序性能越好；数据越接近有序，快速排序性能越差。
class QuickSort:
    def Quick(self, array, low, high):
        if low < high:  # 定义左右指针，当左右指针不重合时才迭代排序
            key_index = self.Partion(array, low, high)
            self.Quick(array, low, key_index)
            self.Quick(array, key_index + 1, high)
        return array

    def Partion(self, array, low, high):
        key = array[low]    # base元素定义为左指针指向的元素
        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            if low < high:
                array[low] = array[high]

            while low < high and array[low] < key:
                low += 1
            if low < high:
                array[high] = array[low]

        array[low] = key
        return low


if __name__ == '__main__':
    array = [2, 3, 4, 7, 1, 6, 5]
    Q = QuickSort()
    print(Q.Quick(array, 0, len(array)-1))
