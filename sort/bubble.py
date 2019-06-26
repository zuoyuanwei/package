# 冒泡排序，最坏时间复杂度为O(n^2),两个for循环。
class BubbleSort:
    def Bubble(self, num):
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if num[j] < num[i]:
                    # 使用同时赋值，可以省略中间变量，节省内存。
                    num[i], num[j] = num[j], num[i]
        return num
    # 短冒泡排序法，只要遍历几次列表，排序可以识别排序列表和停止的优点。
    # 解决传统冒泡排序必须在最终位置被知道之前交换项的缺点。
    def ShortBubble(self, num):
        exchange = True
        passnum = len(num)-1
        while passnum > 0 and exchange:
            exchange = False
            for i in range(passnum):
                if num[i] > num[i+1]:
                    exchange = True
                    num[i+1], num[i] = num[i], num[i+1]
            passnum -= 1
        return num


if __name__ == '__main__':
    num = [5, 2, 4, 6, 1, 3]
    B = BubbleSort()
    print(B.ShortBubble(num))