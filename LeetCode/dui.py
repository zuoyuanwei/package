建立堆
得到堆顶元素，为最大元素
去掉堆顶元素，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序
堆顶元素为第二大元素
重复步骤3，直到堆变空

list = [2,3,1,4,5]
# 堆排序
def heap_sort(list):
    # 初始建堆
    build_max_heap(list, len(list))
    # n-1趟的交换和建堆过程
    for i in range(1, len(list))[::-1]:
        # 将堆顶元素list[0]和最后一个元素list[i]交换
        list[i], list[0] = list[0], list[i]
        # 把剩余的i-1个元素整理成堆
        adjust_down(list, 0, i)
    return list


# 创建堆
# n个节点的完全二叉树，最后一个节点是第n/2个节点的孩子。
# 对于大根堆，若根节点的关键字小于左右子女中关键字较大者，则交换，使该子树成为堆。
# 之后向前依次对各节点（（size/2）-1~1）为根的子树进行筛选。
def build_max_heap(list, size):
    # 从size/2~1,反复调整堆。
    for i in range(0, size // 2)[::-1]:
        adjust_down(list, i, size)


# 调整堆
def adjust_down(list, i, size):
    max = i
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    if rchild < size:
        if lchild < size and list[lchild] > list[max]:
            max = lchild
        if rchild < size and list[rchild] > list[max]:
            max = rchild
        if max != i:
            list[max], list[i] = list[i], list[max]
            # 继续向下调整堆
            adjust_down(list, max, size)

if __name__ == '__main__':
    heap_sort(list)
    print(list)