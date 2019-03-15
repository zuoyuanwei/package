# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sums = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sums += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)
        qiusum(n)
        return self.sums
