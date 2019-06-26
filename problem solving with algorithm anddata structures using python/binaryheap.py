# 二叉堆，堆属性为根节点的值比子节点的值大。
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 堆属性的维护。i//2为当前节点的父节点索引。
    # 将根节点和最小的子节点交换。
    def perUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2]
        i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.perUp(self.currentSize)

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1


bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

