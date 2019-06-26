# 插入排序，最坏情况运行时间为O(n^2)，两个循环。
class InsertionSort:
    def Insertion(self, num):
        for i in range(1, len(num)):
            key = num[i]
            j = i - 1
            while j >= 0 and num[j] > key:
                num[j+1] = num[j]
                j -= 1
            num[j+1] = key
        return num


if __name__ == "__main__":
    num = [5, 2, 4, 6, 1, 3]
    I = InsertionSort()
    print(I.Insertion(num))