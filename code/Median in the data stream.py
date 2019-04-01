如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
Tips：注意self的使用。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):		# A为类的内置属性
        self.A = []
    def Insert(self, num):
        # write code here
        if num is not None:
            return self.A.append(num)		# 类内部可以访问内置属性
    def GetMedian(self,A):			# 类的方法中传入A
        # write code here
        if len(self.A)%2 != 0:
            return sorted(self.A)[(len(self.A))//2]
        else:
            return (sorted(self.A)[len(self.A)//2-1]+sorted(self.A)[len(self.A)//2])/2.0