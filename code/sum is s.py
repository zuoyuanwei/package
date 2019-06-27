# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? 
# Good Luck!
# 输出描述:
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序。

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        max = int((2*tsum)**0.5+1)
        B = []
        for n in range(2,max):
            A = [None for j in range(n)]
            if n%2 != 0:
                A[(n-1)//2] = tsum//n
                for i in range((n-1)//2, n-1):
                    A[i+1] = A[i] + 1
                for i in reversed(range(1, (n-1)//2 + 1)):
                    A[i-1] = A[i] - 1
            else:
                A[n//2 -1] = tsum//n
                for i in range(n//2 -1, n-1):
                    A[i+1]=A[i]+1
                for i in reversed(range(1, n//2+1)):
                    A[i-1] = A[i]-1
            if sum(A) == tsum:
                B.append(A)
        return sorted(B)
