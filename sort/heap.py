# 堆排序，使用最大堆排序，最坏时间复杂度为O(nlgn)。
class Heap:
    def Max_Heapify(self, heap, HeapSize, root):    # 在堆中做结构调整使得父节点的值大于子节点。维护最大堆的性质。
        left = 2*root + 1
        right = 2*root + 1
        larger = root
        if left < HeapSize and heap[larger] < heap[left]:
            larger = left
        if right < HeapSize and heap[larger] < heap[right]:
            larger = right
        if larger != root:      # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            heap[larger], heap[root] = heap[root], heap[larger]
            self.Max_Heapify(heap, HeapSize, larger)
    def Build_Max_Heap(self, heap):
        HeapSize = len(heap)
        for i in range((HeapSize - 2)//2, -1, -1):
            self.Max_Heapify(heap, HeapSize, i)
    def HeapSort(self, heap):
        self.Build_Max_Heap(heap)
        for i in range(len(heap)-1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.Max_Heapify(heap, i, 0)
        return heap


if __name__ == '__main__':
    heap = [5, 2, 4, 6, 1, 3, 7]
    H = Heap()
    print(H.HeapSort(heap))