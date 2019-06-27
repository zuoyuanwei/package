# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sums = 0

    def Sum_Solution(self, n):
        self.sums += n
        while n > 0:
            return self.Sum_Solution(n - 1)
        return self.sums
