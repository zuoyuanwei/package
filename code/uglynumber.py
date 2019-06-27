# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
# (暴力算法:将当前丑数分别乘以2，3，5，再取最小数添加到当前丑数中作为新的丑数，迭代下去)

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        num = [1]
        while len(num) < index:
            m2 = [i*2 for i in num]
            for i in m2:
                if i > num[-1]:
                    m2 = i
                    break
            m3 = [i*3 for i in num]
            for i in m3:
                if i > num[-1]:
                    m3 = i
                    break
            m5 = [i*5 for i in num]
            for i in m5:
                if i > num[-1]:
                    m5 = i
                    break
            num.append(min(m2,m3,m5))
        return num[index-1]
